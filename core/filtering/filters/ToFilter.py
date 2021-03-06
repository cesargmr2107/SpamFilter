import logging

from core.EmailEnvelope import EmailEnvelope
from core.filtering.filters.Filter import Filter


class ToFilter(Filter):

    def filter(self, envelope: EmailEnvelope) -> bool:
        """
        This filter checks whether the envelope recipients are the same as the email message recipients.
        If not, this indicates that the email may be spam.

        :param envelope: The message to be filtered
        :return: False if the recipients are the same, True if else (Spam)
        """

        msg_tos = envelope.get_parsed_to_list()

        if set(envelope.rcpt_tos) != set(msg_tos):
            logging.info(f"Recipients differ: {envelope.rcpt_tos} in envelope VS. {msg_tos} in message")
            return True

        return False
