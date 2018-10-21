column_width = 480
styles = """
body {
    margin: 0;
    font: 12px/18px 'Open Sans',"Lucida Grande","Lucida Sans Unicode",Arial,Helvetica,Verdana,sans-serif;
}
.page_body {
    padding-top: 64px;
    width: %spx;
    margin: 0 auto;
}
.history {
    padding: 16px 0;
}
.message {
    margin: 0 -10px;
    transition: background-color 2.0s ease;
}
.default {
padding: 10px
}
.default .from_name {

    color: #3892db;
    font-weight: 700;
    padding-bottom: 5px;

}
.details {

    color: #70777b;

}
.pull_right {

    float: right;

}
.photo {
max-width: %spx;
}
.body {
margin-left: 40px;
}

.page_header .content .text {

    padding: 24px 24px 22px 24px;
    font-size: 22px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;

}
.bold {

    color: #212121;
    font-weight: 700;

}
.page_header .content {

    width: 480px;
    margin: 0 auto;
    border-radius: 0 !important;

}
.page_header {

    position: fixed;
    z-index: 10;
    background-color: #ffffff;
    width: 100%%;
    border-bottom: 1px solid #e3e6e8;

}
""" % (column_width, column_width - 20)

header = """
<html lang="en">
<head>
  <meta charset="utf-8">

  <title>{}</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">
  <style type="text/css">{}</style>

</head>

<body>
  <div class="page_header">

   <div class="content">

    <div class="text bold">
 {}
    </div>

   </div>

  </div>
<div class="page_body chat_page">
<div class='history'>
"""

footer = """
</div>
</div>
</body>
</html>
"""

basic_message_template = """
<div class="message default clearfix" id="message-{message_id}" >
    <div class="body">
        <div class="pull_right date details" title="{full_date}">
            {time}
        </div>
        <div class="from_name">
            {from_name}
        </div>
        {body}
    </div>
</div>
"""

normal_body_template = """
<div class="text">{text}</div>
"""
photo_body_template = """
<div class="img_body">
    <a href="{img_path}"> <img class='photo' src="{img_path}"></img></a>
</div>
"""

forwaded_wrapper_template = """
<div class="body">
    <div class="from_name">
        {forward_from} <span class='details'>{date}</span>
    </div>
    {body}
</div>
"""
