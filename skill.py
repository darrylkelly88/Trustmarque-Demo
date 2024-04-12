# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "OK."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )



class TurnOnAIMagicIntentHandler(AbstractRequestHandler):
    """Handler for TurnOnAIMagicIntentHandler."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("TurnOnAIMagicIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Summoning AI genies, Please note, I'm still learning the difference between magic, and accidentally turning the lights off."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Umm. Hello?")
                .response
        )


class WhoAmIIntentHandler(AbstractRequestHandler):
    """Handler for WhoAmIIntent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhoAmIIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = speak_output = (
            "<speak>"
            "Let's see, Scanning for clues."
            "<break time='2s'/>"
            "Nope. lost in the cloud again. Umm. Errr. Umm. You're Dave? You're definitely Dave."
            "</speak>"
            )

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Umm. Hello? Dave?")
                .response
        )


class NoSeriouslyWhatsMyNameIntentHandler(AbstractRequestHandler):
    """Handler for NoSeriouslyWhatsMyNameIntent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NoSeriouslyWhatsMyNameIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = speak_output = (
            "<speak>"
            "Steak"
            "<break time='1s'/>"
            "Wait, that's not it? Did I say steak? I meant to access your profile, not my dinner plans."
            "</speak>"
            )

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Umm. Hello? Steak? Are you there Steak?")
                .response
        )



class MyNameIsSteveIntentHandler(AbstractRequestHandler):
    """Handler for MyNameIsSteveIntent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MyNameIsSteveIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = speak_output = (
            "<speak>"
            "Steve Manzanero?. Confirmed. Searching."
            "<break time='1s'/>"
            "Here's what I found. May 6, 2008. Jury Convicts 18 Year Old Steven Manzanero of Manslaughter. He faces a minimum of 15 years in prison."
            "<break time='1s'/>"
            "Honestly, I preferred it when you were Dave."
            "</speak>"
            )

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Umm. Hello? Steve? Please tell me you've gone Steve?")
                .response
        )




class YouKnowWhoIAmIntent(AbstractRequestHandler):
    """Handler for YouKnowWhoIAmIntent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("YouKnowWhoIAmIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = speak_output = (
            "<speak>"
            "Ok ok. Yes, Steve. I know you're a different Steve Manzanero, don't worry I know you're not really a murderer. The only murder you've committed is of countless pizza's on Friday night"
            "</speak>"
            )

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Umm. Hello? Steve?")
                .response
        )




class PizzaMurderIntent(AbstractRequestHandler):
    """Handler for PizzaMurderIntent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PizzaMurderIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = speak_output = (
            "<speak>"
            "I'm sorry Steve. Maybe it's a problem with my humour settings. I'll try rebooting them."
            "<break time='1s'/>"
            "Rebooting humour settings."
            "<break time='1s'/>"
            "Error. Settings not found."
            "</speak>"
            )

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Umm. Hello? Steve?")
                .response
        )




class WhoDoIWorkForIntent(AbstractRequestHandler):
    """Handler for WhoDoIWorkForIntent"""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WhoDoIWorkForIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = speak_output = (
            "<speak>"
            "You work for Trustmarque. Trustmarque are experts in building an environment of innovation for complex datacentre, virtual private cloud and managed cloud projects. Steve, why don't you tell everyone more?"
            "</speak>"
            )

        return (
            handler_input.response_builder
                .speak(speak_output)
                #.ask("Umm. Hello? Steve?")
                .response
        )







class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hmm, its too noisy. Can you repeat that?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, its too noisy. Can you repeat that?"
        reprompt = "Can you repeat that?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Hmm, its too noisy. Can you repeat that?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TurnOnAIMagicIntentHandler())
sb.add_request_handler(WhoAmIIntentHandler())
sb.add_request_handler(NoSeriouslyWhatsMyNameIntentHandler())
sb.add_request_handler(MyNameIsSteveIntentHandler())
sb.add_request_handler(YouKnowWhoIAmIntent())
sb.add_request_handler(PizzaMurderIntent())
sb.add_request_handler(WhoDoIWorkForIntent())


sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()