self.webpackChunk(["mode/jsx"],{34:function(a,b,c){(function(a){a(c(0),c(3),c(4))})(function(a){"use strict";function b(a,b,c,d){this.state=a,this.mode=b,this.depth=c,this.prev=d}function c(d){return new b(a.copyState(d.mode,d.state),d.mode,d.depth,d.prev&&c(d.prev))}a.defineMode("jsx",function(d,e){function f(a){var b=a.tagName;a.tagName=null;var c=j.indent(a,"");return a.tagName=b,c}function g(a,b){return b.context.mode==j?h(a,b,b.context):i(a,b,b.context)}function h(c,e,h){if(2==h.depth)return c.match(/^.*?\*\//)?h.depth=1:c.skipToEnd(),"comment";if("{"==c.peek()){j.skipAttribute(h.state);var i=f(h.state),l=h.state.context;if(l&&c.match(/^[^>]*>\s*$/,!1)){for(;l.prev&&!l.startOfLine;)l=l.prev;l.startOfLine?i-=d.indentUnit:h.prev.state.lexical&&(i=h.prev.state.lexical.indented)}else 1==h.depth&&(i+=d.indentUnit);return e.context=new b(a.startState(k,i),k,0,e.context),null}if(1==h.depth){if("<"==c.peek())return j.skipAttribute(h.state),e.context=new b(a.startState(j,f(h.state)),j,0,e.context),null;if(c.match("//"))return c.skipToEnd(),"comment";if(c.match("/*"))return h.depth=2,g(c,e)}var m,n=j.token(c,h.state),o=c.current();return /\btag\b/.test(n)?/>$/.test(o)?h.state.context?h.depth=0:e.context=e.context.prev:/^</.test(o)&&(h.depth=1):!n&&-1<(m=o.indexOf("{"))&&c.backUp(o.length-m),n}function i(c,d,e){if("<"==c.peek()&&k.expressionAllowed(c,e.state))return k.skipExpression(e.state),d.context=new b(a.startState(j,k.indent(e.state,"")),j,0,d.context),null;var f=k.token(c,e.state);if(!f&&null!=e.depth){var g=c.current();"{"==g?e.depth++:"}"==g&&0==--e.depth&&(d.context=d.context.prev)}return f}var j=a.getMode(d,{name:"xml",allowMissing:!0,multilineTagIndentPastTag:!1,allowMissingTagName:!0}),k=a.getMode(d,e&&e.base||"javascript");return{startState:function(){return{context:new b(a.startState(k),k)}},copyState:function(a){return{context:c(a.context)}},token:g,indent:function(a,b,c){return a.context.mode.indent(a.context.state,b,c)},innerMode:function(a){return a.context}}},"xml","javascript"),a.defineMIME("text/jsx","jsx"),a.defineMIME("text/typescript-jsx",{name:"jsx",base:{name:"javascript",typescript:!0}})})}});
//# sourceMappingURL=jsx.js.map