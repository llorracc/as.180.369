import{c as d}from"/dockervm24/ed921311-9af1-11ef-8c58-5254001d4703/proxy/3000/build/_shared/chunk-2NH4LW52.js";var g=d((m,c)=>{function u(e){let a="[a-zA-Z_][\\w.]*",n="<\\?(lasso(script)?|=)",r="\\]|\\?>",s={$pattern:a+"|&[lg]t;",literal:"true false none minimal full all void and or not bw nbw ew new cn ncn lt lte gt gte eq neq rx nrx ft",built_in:"array date decimal duration integer map pair string tag xml null boolean bytes keyword list locale queue set stack staticarray local var variable global data self inherited currentcapture givenblock",keyword:"cache database_names database_schemanames database_tablenames define_tag define_type email_batch encode_set html_comment handle handle_error header if inline iterate ljax_target link link_currentaction link_currentgroup link_currentrecord link_detail link_firstgroup link_firstrecord link_lastgroup link_lastrecord link_nextgroup link_nextrecord link_prevgroup link_prevrecord log loop namespace_using output_none portal private protect records referer referrer repeating resultset rows search_args search_arguments select sort_args sort_arguments thread_atomic value_list while abort case else fail_if fail_ifnot fail if_empty if_false if_null if_true loop_abort loop_continue loop_count params params_up return return_value run_children soap_definetag soap_lastrequest soap_lastresponse tag_name ascending average by define descending do equals frozen group handle_failure import in into join let match max min on order parent protected provide public require returnhome skip split_thread sum take thread to trait type where with yield yieldhome"},t=e.COMMENT("<!--","-->",{relevance:0}),i={className:"meta",begin:"\\[noprocess\\]",starts:{end:"\\[/noprocess\\]",returnEnd:!0,contains:[t]}},l={className:"meta",begin:"\\[/noprocess|"+n},_={className:"symbol",begin:"'"+a+"'"},o=[e.C_LINE_COMMENT_MODE,e.C_BLOCK_COMMENT_MODE,e.inherit(e.C_NUMBER_MODE,{begin:e.C_NUMBER_RE+"|(-?infinity|NaN)\\b"}),e.inherit(e.APOS_STRING_MODE,{illegal:null}),e.inherit(e.QUOTE_STRING_MODE,{illegal:null}),{className:"string",begin:"`",end:"`"},{variants:[{begin:"[#$]"+a},{begin:"#",end:"\\d+",illegal:"\\W"}]},{className:"type",begin:"::\\s*",end:a,illegal:"\\W"},{className:"params",variants:[{begin:"-(?!infinity)"+a,relevance:0},{begin:"(\\.\\.\\.)"}]},{begin:/(->|\.)\s*/,relevance:0,contains:[_]},{className:"class",beginKeywords:"define",returnEnd:!0,end:"\\(|=>",contains:[e.inherit(e.TITLE_MODE,{begin:a+"(=(?!>))?|[-+*/%](?!>)"})]}];return{name:"Lasso",aliases:["ls","lassoscript"],case_insensitive:!0,keywords:s,contains:[{className:"meta",begin:r,relevance:0,starts:{end:"\\[|"+n,returnEnd:!0,relevance:0,contains:[t]}},i,l,{className:"meta",begin:"\\[no_square_brackets",starts:{end:"\\[/no_square_brackets\\]",keywords:s,contains:[{className:"meta",begin:r,relevance:0,starts:{end:"\\[noprocess\\]|"+n,returnEnd:!0,contains:[t]}},i,l].concat(o)}},{className:"meta",begin:"\\[",relevance:0},{className:"meta",begin:"^#!",end:"lasso9$",relevance:10}].concat(o)}}c.exports=u});export default g();
