/**
 * Copyright 2020 Amazon.com, Inc. and its affiliates. All Rights Reserved.
 * SPDX-License-Identifier: LicenseRef-.amazon.com.-AmznSL-1.0
 *
 * Licensed under the Amazon Software License (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 * http://aws.amazon.com/asl/
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 **/
const Alexa = require('ask-sdk-core');
const i18next = require('i18next');
const sprintf = require('sprintf-js').sprintf;
const RESOURCES = require('./resources');
const util = require('./util');

/**
 * API Handler for RecordColor API
 *
 * @param handlerInput
 * @returns API response object
 *
 * See https://developer.amazon.com/en-US/docs/alexa/conversations/handle-api-calls.html
 */
const RecordColorApiHandler = {
    canHandle(handlerInput) {
        return util.isApiRequest(handlerInput, 'RecordColor');
    },
    handle(handlerInput) {
        console.log("Api Request [RecordColor]: ", JSON.stringify(handlerInput.requestEnvelope.request, null, 2));
        // First get our request entity and grab the color passed in the API call
        const args = util.getApiArguments(handlerInput);
        const color = args.color;
        // Store the favorite color in the session
        const sessionAttributes = handlerInput.attributesManager.getSessionAttributes();
        sessionAttributes.favoriteColor = color;

        const locale = handlerInput.requestEnvelope.request.locale;
        const response = {
            apiResponse: {
                color: color,
                displayLocale: locale
            }
        };
        console.log("Api Response [RecordColor]: ", JSON.stringify(response, null, 2));
        return response;
    }
}

const IntroToAlexaConversationsButtonEventHandler = {
    canHandle(handlerInput){
        console.log(JSON.stringify(handlerInput.requestEnvelope));
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'Alexa.Presentation.APL.UserEvent'
            && handlerInput.requestEnvelope.request.arguments[0] === 'SetFavoriteColor';
    },
    handle(handlerInput){
        return handlerInput.responseBuilder
            .addDirective({
                type: 'Dialog.DelegateRequest',
                target: 'AMAZON.Conversations',
                period: {
                    until: 'EXPLICIT_RETURN'
                },
                updatedRequest: {
                    type: 'Dialog.InputRequest',
                    input: {
                        name: 'SpecifyFavoriteColor',
                        slots: {
                            name: {
                                name : 'color',
                                value: handlerInput.requestEnvelope.request.arguments[1]
                            }
                        }
                    }
                }
            })
            .getResponse();
    }
}

/**
 * API Handler for GetFavoriteColor API
 *
 * @param handlerInput
 * @returns API response object
 *
 * See https://developer.amazon.com/en-US/docs/alexa/conversations/handle-api-calls.html
 */
const GetFavoriteColorApiHandler = {
    canHandle(handlerInput) {
        return util.isApiRequest(handlerInput, 'GetFavoriteColor');
    },
    handle(handlerInput) {
        console.log("Api Request [GetFavoriteColor]: ", JSON.stringify(handlerInput.requestEnvelope.request, null, 2));

        // Get the favorite color from the session
        const sessionAttributes = handlerInput.attributesManager.getSessionAttributes();
        const color = sessionAttributes.favoriteColor ? sessionAttributes.favoriteColor : null;
        const locale = handlerInput.requestEnvelope.request.locale;
        const response = {
            apiResponse: {
                color: color,
                displayLocale: locale
            }
        };

        console.log("Api Response [GetFavoriteColor]: ", JSON.stringify(response, null, 2));
        return response;
    }
}

/**
 * FallbackIntentHandler - Handle all other requests to the skill when Conversations is not the focused dialog manager.
 *
 * @param handlerInput
 * @returns response
 *
 * See https://developer.amazon.com/en-US/docs/alexa/conversations/handle-api-calls.html
 */
const FallbackIntentHandler = {
    canHandle(handlerInput) {
        const request = handlerInput.requestEnvelope.request;
        return request.type === 'IntentRequest' && request.intent.name !== 'GetFavoriteColorApiHandler' && request.intent.name !== 'RecordColorApiHandler';
    },
    handle(handlerInput) {
        const intentName = handlerInput.requestEnvelope.request.intent.name;
        console.log('In catch all intent handler. Intent invoked: ' + intentName);
        const speechOutput = handlerInput.t('FALLBACK_RESPONSE');

        return handlerInput.responseBuilder
            .speak(speechOutput)
            .reprompt(speechOutput)
            .getResponse();
    },
};

const SessionEndedRequestHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'SessionEndedRequest';
    },
    handle(handlerInput) {
        // Any cleanup logic goes here.
        return handlerInput.responseBuilder.getResponse();
    }
};

// Generic error handling to capture any syntax or routing errors. If you receive an error
// stating the request handler chain is not found, you have not implemented a handler for
// the intent being invoked or included it in the skill builder below.
const ErrorHandler = {
    canHandle() {
        return true;
    },
    handle(handlerInput, error) {
        console.log(`~~~~ Error handled: ${error.stack}`);
        const speakOutput = handlerInput.t('ERROR_RESPONSE');

        return handlerInput.responseBuilder
            .speak(speakOutput)
            .reprompt(speakOutput)
            .getResponse();
    }
};

// *****************************************************************************
// These simple interceptors just log the incoming and outgoing request bodies to assist in debugging. The localization
// interceptor adds a t()-delegating method to localize strings.

const LogRequestInterceptor = {
    process(handlerInput) {
        console.log(`REQUEST ENVELOPE = ${JSON.stringify(handlerInput.requestEnvelope)}`);
    },
};

const LocalizationInterceptor = {
    process(handlerInput) {
        i18next.init({
            lng: handlerInput.requestEnvelope.request.locale,
            fallbackLng: 'en',
            overloadTranslationOptionHandler: sprintf.overloadTranslationOptionHandler,
            resources: RESOURCES,
            returnObjects: true
        });

        const baseOpts = {
            interpolation: {
                escapeValue: false
            }
        };

        handlerInput.t = (key, opts) => {
            const value = i18next.t(key, {
                ...baseOpts,
                ...opts
            });

            if (Array.isArray(value)) {
                return value[Math.floor(Math.random() * value.length)];
            } else {
                return value;
            }
        };
    }
};

const LogResponseInterceptor = {
    process(handlerInput, response) {
        console.log(`RESPONSE = ${JSON.stringify(response)}`);
    },
};

// The SkillBuilder acts as the entry point for your skill, routing all request and response
// payloads to the handlers above. Make sure any new handlers or interceptors you've
// defined are included below. The order matters - they're processed top to bottom.
exports.handler = Alexa.SkillBuilders.custom()
    .addErrorHandlers(ErrorHandler)
    .addRequestInterceptors(LogRequestInterceptor, LocalizationInterceptor)
    .addResponseInterceptors(LogResponseInterceptor)
    .addRequestHandlers(
        RecordColorApiHandler,
        GetFavoriteColorApiHandler,
        IntroToAlexaConversationsButtonEventHandler,
        FallbackIntentHandler,
        SessionEndedRequestHandler
    )
    .withCustomUserAgent('reference-skills/intro-to-alexa-conversations/v1')
    .lambda();
