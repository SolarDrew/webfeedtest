# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1501508204.0467908
_enable_loop = True
_template_filename = '/home/drew/anaconda3/envs/nikola/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl'
_template_uri = 'comments_helper_isso.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_form', 'comment_link_script', 'comment_link']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <div data-title="')
            __M_writer(filters.url_escape(str(title)))
            __M_writer('" id="isso-thread"></div>\n        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/embed.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        pagekind = context.get('pagekind', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id and 'index' in pagekind:
            __M_writer('        <script src="')
            __M_writer(str(comment_system_id))
            __M_writer('js/count.min.js" data-isso="')
            __M_writer(str(comment_system_id))
            __M_writer('"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system_id:
            __M_writer('        <a href="')
            __M_writer(str(link))
            __M_writer('#isso-thread">Comments</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "filename": "/home/drew/anaconda3/envs/nikola/lib/python3.4/site-packages/nikola/data/themes/base/templates/comments_helper_isso.tmpl", "line_map": {"66": 9, "71": 9, "72": 10, "73": 11, "74": 11, "75": 11, "16": 0, "81": 75, "21": 7, "22": 13, "23": 20, "29": 2, "34": 2, "35": 3, "36": 4, "37": 4, "38": 4, "39": 5, "40": 5, "41": 5, "42": 5, "48": 16, "54": 16, "55": 17, "56": 18, "57": 18, "58": 18, "59": 18, "60": 18}, "uri": "comments_helper_isso.tmpl"}
__M_END_METADATA
"""
