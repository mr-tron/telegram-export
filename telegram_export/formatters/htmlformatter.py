"""
Formatter to display paginated(?) HTML of a context.
Very much unfinished and needs a web designer to work on it.
"""
from . import BaseFormatter

import utils as export_utils
from .htmltemplates import *


class HtmlFormatter(BaseFormatter):
    """A Formatter class to generate HTML"""
    @staticmethod
    def name():
        return 'html'

    def output_header(self, file, context):
        """Output the header of the page. Context should be a namedtuple"""
        name = self.get_display_name(context)

        print(header.format(name, styles, name), file=file)

    def generate_message_html(self, message, context):
        """
        Return HTML for a message, showing reply message, forward headers,
        view count, post author, and media (if applicable).
        """
        from_name = self.get_display_name(message.from_id) or "(???)"

        if message.media_id:
            media = self.get_media(message.media_id)
            if media.type == 'photo':

                media_path = "%s-%s.%s%s" % (media.type, media.name, media.id,
                                             export_utils.get_extension(media.mime_type))
                media_path = 'usermedia/%s-%s/%s' %(self.get_display_name(context), context.id, media_path)
                body = photo_body_template.format(img_path=media_path)
            else:
                text = "Unsupported media type: %s. Message_id: %s, media_id: %s" % \
                       (media.type, message.id, media.id)
                body = normal_body_template.format(text=text)
        else:
            text = message.text
            body = normal_body_template.format(text=text)
        if message.forward_id:
            forward = self.get_forward(message.forward_id)
            body = forwaded_wrapper_template.format(
                forward_from=self.get_human_readable_forwarded(forward),
                body=body,
                date=forward.original_date)
        rendered = basic_message_template.format(
            message_id=message.id,
            from_name=from_name,
            body=body,
            full_date=message.date,
            time=message.date.strftime("%H:%M"))

        return rendered

    def _format(self, context_id, file, *args, **kwargs,):
        """Format the given context as HTML and output to 'file'"""
        entity = self.get_entity(context_id)
        # file = sys.stdout
        self.output_header(file, entity)
        for message in self.get_messages_from_context(context_id,
                                                      order='ASC'):
            print(self.generate_message_html(message, entity), file=file)
        print(footer, file=file)