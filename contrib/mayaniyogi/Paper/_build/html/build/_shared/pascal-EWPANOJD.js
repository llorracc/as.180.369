import{b as c}from"/dockervm24/ed921311-9af1-11ef-8c58-5254001d4703/proxy/3000/build/_shared/chunk-2NH4LW52.js";function s(r){for(var n={},e=r.split(" "),t=0;t<e.length;++t)n[e[t]]=!0;return n}function p(r,n){var e=r.next();if(e=="#"&&n.startOfLine)return r.skipToEnd(),"meta";if(e=='"'||e=="'")return n.tokenize=k(e),n.tokenize(r,n);if(e=="("&&r.eat("*"))return n.tokenize=l,l(r,n);if(e=="{")return n.tokenize=u,u(r,n);if(/[\[\]\(\),;\:\.]/.test(e))return null;if(/\d/.test(e))return r.eatWhile(/[\w\.]/),"number";if(e=="/"&&r.eat("/"))return r.skipToEnd(),"comment";if(a.test(e))return r.eatWhile(a),"operator";r.eatWhile(/[\w\$_]/);var t=r.current();return f.propertyIsEnumerable(t)?"keyword":d.propertyIsEnumerable(t)?"atom":"variable"}function k(r){return function(n,e){for(var t=!1,i,o=!1;(i=n.next())!=null;){if(i==r&&!t){o=!0;break}t=!t&&i=="\\"}return(o||!t)&&(e.tokenize=null),"string"}}function l(r,n){for(var e=!1,t;t=r.next();){if(t==")"&&e){n.tokenize=null;break}e=t=="*"}return"comment"}function u(r,n){for(var e;e=r.next();)if(e=="}"){n.tokenize=null;break}return"comment"}var f,d,a,b,m=c(()=>{f=s("absolute and array asm begin case const constructor destructor div do downto else end file for function goto if implementation in inherited inline interface label mod nil not object of operator or packed procedure program record reintroduce repeat self set shl shr string then to type unit until uses var while with xor as class dispinterface except exports finalization finally initialization inline is library on out packed property raise resourcestring threadvar try absolute abstract alias assembler bitpacked break cdecl continue cppdecl cvar default deprecated dynamic enumerator experimental export external far far16 forward generic helper implements index interrupt iocheck local message name near nodefault noreturn nostackframe oldfpccall otherwise overload override pascal platform private protected public published read register reintroduce result safecall saveregisters softfloat specialize static stdcall stored strict unaligned unimplemented varargs virtual write"),d={null:!0},a=/[+\-*&%=<>!?|\/]/;b={name:"pascal",startState:function(){return{tokenize:null}},token:function(r,n){if(r.eatSpace())return null;var e=(n.tokenize||p)(r,n);return e=="comment"||e=="meta",e},languageData:{indentOnInput:/^\s*[{}]$/,commentTokens:{block:{open:"(*",close:"*)"}}}}});m();export{b as pascal};
