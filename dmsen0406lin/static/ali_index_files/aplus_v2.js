!function e(t,n,r){function a(i,u){if(!n[i]){if(!t[i]){var s="function"==typeof require&&require;if(!u&&s)return s(i,!0);if(o)return o(i,!0);throw new Error("Cannot find module '"+i+"'")}var l=n[i]={exports:{}};t[i][0].call(l.exports,function(e){var n=t[i][1][e];return a(n?n:e)},l,l.exports,e,t,n,r)}return n[i].exports}for(var o="function"==typeof require&&require,i=0;i<r.length;i++)a(r[i]);return a}({1:[function(e,t,n){"use strict";function r(e,t){return e&&e.getAttribute?e.getAttribute(t)||"":""}function a(e){return i=i||document.getElementsByTagName("head")[0],u&&!e?u:i?u=i.getElementsByTagName("meta"):[]}function o(e){var t,n,o,i=a(),u=i.length;for(t=0;u>t;t++)n=i[t],r(n,"name")===e&&(o=r(n,"content"));return o||""}var i,u,s=e("@ali/grey-publish").util;n.tryToGetAttribute=r,n.getMetaTags=a,n.getMetaCnt=o,n.indexof=function(e,t){for(var n=0;n<e.length;n++)if(e[n]===t)return n;return-1};var l=function(e,t){return e+="",e.length<t&&(e="0"+e),e};n.getDateMin=function(){var e=new Date,t="";return t+=e.getFullYear(),t+=l(e.getMonth()+1,2),t+=l(e.getDate(),2),t+=l(e.getHours(),2),t+=l(e.getMinutes(),2)},n.loopAddScript=function(e,t){try{if(t&&t instanceof Array){var n=0,r=function(a){a&&s.addScript(e+"/"+a,function(){r(t[++n])})};r(t[n])}}catch(a){}},n.getCdnpath=function(){var e=document,t=e.getElementById("beacon-aplus")||e.getElementById("tb-beacon-aplus"),n="//g.alicdn.com",r=["//assets.alicdn.com/g","//g-assets.daily.taobao.net","//u.alicdn.com","//laz-g-cdn.alicdn.com"],a=new RegExp("//u.alicdn.com");if(t)for(var o=0;o<r.length;o++){var i=new RegExp(r[o]);if(i.test(t.src)){n=r[o],a.test(t.src)&&(n="//assets.alicdn.com/g");break}}return n},n.aplusVersions={V_O:"aplus_o.js",V_2:"aplus_v2.js",V_W:"aplus_wap.js",V_S:"aplus_std.js",V_I:"aplus_int.js",V_U:"aplus_u.js"}},{"@ali/grey-publish":2}],2:[function(e,t,n){"use strict";n.grey=e("./src/grey"),n.util=e("./src/util")},{"./src/grey":3,"./src/util":4}],3:[function(e,t,n){"use strict";function r(e,t){return e+Math.floor(Math.random()*(t-e+1))}function a(e){var t=!1;try{var n=e.bingo_chars||"0aAbBc1CdDeE2fFgGh3HiIjJ4kKlLm5MnNoO6pPqQr7RsStT8uUvVw9WxXyY+zZ",a=l.getCookie(e.bingo_cookiename||"cna")||"";if(a){var o=a.charAt(0),i=n.indexOf(o)/n.length;t=i<=e.ratio/e.base}else t=r(1,e.base)<=e.ratio}catch(u){t=r(1,e.base)<=e.ratio}return t}function o(e,t){var n;for(n in t)t.hasOwnProperty(n)&&(e[n]=t[n]);return e}function i(e,t){return function(n){return e(o(t,n||{}))}}function u(e){var t=window,n=document;if(e)try{var r=n.getElementsByTagName("script")[0],a=n.createElement("script");a.appendChild(n.createTextNode(e)),r.parentNode.insertBefore(a,r)}catch(o){try{(t.execScript||function(e){t.eval(e)})(e)}catch(i){}}}function s(e,t,n){try{var r=[],a=p.get(t);if(a){var o=JSON.parse(a)||[];if(o&&o.length>0)for(var i=new RegExp("^"+n),u=0;u<o.length;u++)i.test(o[u])?r.push(o[u]):p.remove(o[u])}r.push(e),p.set(t,JSON.stringify(r))}catch(s){}}var l=e("./util"),c=function(){},g=function(e){return"function"==typeof e},p={set:function(e,t){try{return localStorage.setItem(e,t),!0}catch(n){return!1}},get:function(e){return localStorage.getItem(e)},test:function(){var e="grey_test_key";try{return localStorage.setItem(e,1),localStorage.removeItem(e),!0}catch(t){return!1}},remove:function(e){localStorage.removeItem(e)}},f={base:1e4},v={_config:f},h=function(e,t){var n=window,r=n.XDomainRequest,a=n.XMLHttpRequest&&"withCredentials"in new n.XMLHttpRequest,o=t.after;if("function"!=typeof o&&(o=c),!t.isDebug&&p.test()&&(a||r)){var i=t.LS_KEY+l.hash(e),g=p.get(i);if(g)try{u(g),o({from:"local"})}catch(f){l.addScript(e,o)}else{var v=navigator.userAgent;l.request(e,v,function(e){p.set(i,e),s(i,t.LS_KEY_CLUSTER,t.LS_KEY),u(e),o({from:"cors"})},function(){l.addScript(e,o)})}}else l.addScript(e,o)};v.load=function(e){e=o({LS_KEY_CLUSTER:"",LS_KEY:"",isLoadDevVersion:c,dev:"",stable:"",grey:"",base:f.base,bingo:""},e);var t,n={},r="function"==typeof e.bingo?e.bingo:a;return e.ratio>=e.base||r(e)?(t=e.grey,n.type="grey"):(t=e.stable,n.type="stable"),g(e.isLoadDevVersion)&&e.isLoadDevVersion()&&(t=e.dev,n.type="dev"),n.url=t,g(e.before)&&e.before(n),e.after=g(e.after)?i(e.after,n):c,h(t,e),this},v.config=function(e){return o(f,e||{}),this},t.exports=v},{"./util":4}],4:[function(e,t,n){"use strict";var r=function(e,t){var n=document,r=n.getElementsByTagName("script")[0],a=n.getElementsByTagName("head")[0],o=n.createElement("script");o.type="text/javascript",o.async=!0,o.src=e,r?r.parentNode.insertBefore(o,r):a&&a.appendChild(o),"function"==typeof t&&t({from:"script"})};n.addScript=r,n.getCookie=function(e){var t=document,n=t.cookie.match(new RegExp("(?:^|;)\\s*"+e+"=([^;]+)"));return n?n[1]:""};var a={base:1e4,timeout:1e4};n.request=function(e,t,n,r){if(/blitz/i.test(t))return void r();var o,i="GET",u=function(){o.responseText?n(o.responseText):r()},s=window.XMLHttpRequest&&"withCredentials"in new XMLHttpRequest;s?(o=new XMLHttpRequest,o.open(i,e,!0)):(o=new XDomainRequest,o.open(i,e)),o.timeout=a.timeout,o.onload=u,o.onerror=r,o.ontimeout=r,o.send()},n.hash=function(e){var t,n,r=1315423911;for(t=e.length-1;t>=0;t--)n=e.charCodeAt(t),r^=(r<<5)+n+(r>>2);return(2147483647&r).toString(16)}},{}],5:[function(e,t,n){"use strict";!function(){var t=window,n="g_aplus_grey_launched";if(!t[n]){t[n]=1;var r=t.goldlog||(t.goldlog={}),a=e("@ali/grey-publish").grey,o=!1;try{var i=location.href.match(/aplusDebug=(true|false)/);i&&i.length>0&&window.localStorage.setItem("aplusDebug",i[1]),o="true"===window.localStorage.getItem("aplusDebug"),r.aplusDebug=o}catch(u){}var s=e("../grey/util"),l=e("./for_aplus_fns"),c={"aplus_o.js":{stable_version:{value:"8.3.1"},grey_version:{value:"8.3.2"},dev_version:{}},"aplus_std.js":{stable_version:{value:"8.3.1"},grey_version:{value:"8.3.2"},dev_version:{}},"aplus_wap.js":{stable_version:{value:"8.3.1"},grey_version:{value:"8.3.2"},dev_version:{}},"aplus_int.js":{stable_version:{value:"8.3.1"},grey_version:{value:"8.3.2"},dev_version:{}},"aplus_u.js":{stable_version:{value:"8.3.1"},grey_version:{value:"8.3.2"},dev_version:{}}},g="APLUS_S_CORE_0.18.11_20180308002209_",p=location.protocol;0!==p.indexOf("http")&&(p="http:");var f=s.getCdnpath();r.getCdnPath=s.getCdnpath;var v=p+f+"/alilog",h=l.getAplusBuVersion(),d=h.v,_=h.BU,m=1e4,y=[],b=function(){var e="";if(y&&y.length>0)for(var t=s.getDateMin(),n=0;n<y.length;n++){var r=y[n].key+"";t>=r&&(e=Math.floor(1e4*y[n].value))}return e},j=e("./utilPlugins"),w=function(e){var t,n=o?[]:j.getFrontPlugins({version:e,fn:d,BU:_}),r=[["s",e,d].join("/")],a=o?[]:j.getPlugins({version:e,fn:d,BU:_});try{var i=[].concat(n,r,a);t=v+"/??"+i.join(",")+"?v=20180308002209"}catch(u){t=v+"/??"+r.join(",")}return t},S=function(){var e,n="aplus_grey_ratio";"number"==typeof t[n]&&(e=Math.floor(1e4*t[n]));var r=location.search.match(new RegExp("\\b"+n+"=([\\d\\.]+)"));return r&&(r=parseFloat(r[1]),isNaN(r)||(e=Math.floor(1e4*r))),e},V=b(),E=S();V&&(m=V),E&&(m=E),r.aplus_cplugin_ver="0.3.3",r.record||(r.record=function(e,n,r,a){(t.goldlog_queue||(t.goldlog_queue=[])).push({action:"goldlog.record",arguments:[e,n,r,a]})});var B=c[d],x=B.stable_version.value||"7.7.0",L=B.grey_version.value||x,U=B.dev_version.value||L;a.load({LS_KEY_CLUSTER:"APLUS_LS_KEY",LS_KEY:g,isDebug:o,isLoadDevVersion:!1,dev:w(U),stable:w(x),grey:w(L),ratio:m,before:function(e){switch(e.type){case"grey":r.lver=U;break;case"stable":r.lver=x;break;case"dev":r.lver=U}o&&s.loopAddScript(v,j.getFrontPlugins({version:r.lver,fn:d,BU:_}))},after:function(){if(o){var e=0,t=function(){if(!(e>=100)){e++;var n=r._$||{};window.setTimeout(function(){"complete"===n.status?s.loopAddScript(v,j.getPlugins({version:r.lver,fn:d,BU:_})):t()},100)}};t()}}})}}()},{"../grey/util":1,"./for_aplus_fns":6,"./utilPlugins":9,"@ali/grey-publish":2}],6:[function(e,t,n){"use strict";var r=e("./util"),a=r.aplusVersions,o=[a.V_O,a.V_S,a.V_I,a.V_W,a.V_U],i=function(){for(var e,t,n=[{version:a.V_O,domains:[/^https?:\/\/(.*\.)?youku\.com/i,/^https?:\/\/(.*\.)?tudou\.com/i,/^https?:\/\/(.*\.)?soku\.com/i,/^https?:\/\/(.*\.)?laifeng\.com/i],BU:"YT"},{version:a.V_I,domains:[/^https?:\/\/(.*\.)?scmp\.com/i,/^https?:\/\/(.*\.)?luxehomes\.com\.hk/i,/^https?:\/\/(.*\.)?ays\.com\.hk/i,/^https?:\/\/(.*\.)?cpjobs\.com/i,/^https?:\/\/(.*\.)?educationpost\.com\.hk/i,/^https?:\/\/(.*\.)?elle\.com\.hk/i,/^https?:\/\/(.*\.)?harpersbazaar\.com\.hk/i,/^https?:\/\/(.*\.)?esquirehk\.com/i],BU:"SCMP"}],r=0;r<n.length;r++)for(var o=n[r].domains,i=n[r].version,u=0;u<o.length;u++)if(location.href.match(o[u]))return{v:i,BU:n[r].BU};return{v:t,BU:e}},u=function(){var e=r.getMetaCnt("aplus-version");return e&&(e+=".js"),r.indexof(o,e)>-1?e:null},s=function(){try{for(var e=document,t=e.getElementsByTagName("script"),n=0;n<t.length;n++){var r=t[n].getAttribute("src");if(/alilog\/mlog\/aplus_\w+\.js/.test(r)||/alicdn\.com\/js\/aplus_\w+\.js/.test(r))return r}return""}catch(a){return""}},l=function(){var e="";try{var t=document,n=t.getElementById("beacon-aplus")||t.getElementById("tb-beacon-aplus");if(n&&(e=n.getAttribute("src")),e||(e=s()),e){var r=e.match(/aplus_\w+\.js/);"object"==typeof r&&r.length>0&&(e=r[0])}}catch(a){e=""}finally{return e}};n.getAplusBuVersion=function(){var e,t;try{e=a.V_S;var n=l();n&&(e=n);var r=i();r&&r.v&&(e=r.v),t=r.BU;var o=u();o&&(e=o),e===a.V_2&&(e=a.V_S)}catch(s){e=e===a.V_O?a.V_W:a.V_S}finally{return{v:e,BU:t}}}},{"./util":8}],7:[function(e,t,n){"use strict";var r=document,a=window,o=e("./util"),i=o.aplusVersions,u=(e("@ali/grey-publish").util,a.navigator.userAgent),s=/WindVane/i.test(u),l=/AliBaichuan/i.test(u),c=(parent!==self,function(e){return s&&!a.WindVane&&e.fn!==i.V_O}),g=function(e){return(l||s&&!a.WindVane)&&e.fn===i.V_O},p=function(e){var t;if(r.querySelector){var n=r.querySelector("[name=data-spm]");n&&"a1z1d1"===n.getAttribute("content")&&(t=!0)}return t},f=function(e){return e.fn===i.V_O||"YT"===e.BU},v=function(){return/_a_ig_v=@aplus/.test(location.search)},h=function(e){return!0},d=function(e){return e.fn!==i.V_O&&e.fn!==i.V_U},_=function(){try{var e=a.localStorage,t="aplus_track_debug_id",n=new RegExp("[?|&]"+t+"=(\\w*)"),o=location.href.match(n);if(o&&o.length>0)e.setItem(t,o[1]);else{var i=r.referrer||"",u=i.match(n);if(u&&u.length>0)e.setItem(t,u[1]);else{var s=a.name||"",l=s.match(n);l&&l.length>0&&e.setItem(t,l[1])}}var c=e.getItem(t)||"";return c&&c.length>50?!0:!1}catch(g){return!1}},m=function(){try{return!!/lazada/.test(location.host)}catch(e){return!1}},y=function(){try{return/aplus_ws=true/.test(location.search)}catch(e){return!1}};n.getFrontPlugins=function(e){var t="s/"+e.version+"/plugin",n=goldlog.aplus_cplugin_ver;return[{enable:c(e),path:[t,"aplus_windvane2.js"].join("/")},{enable:g(e),path:[t,"aplus_bcbridge.js"].join("/")},{enable:p(e),path:["aplus_cplugin",n,"aplus4ut.js"].join("/")},{enable:!0,path:[t,"aplus_client.js"].join("/")},{enable:!0,path:["aplus_cplugin",n,"toolkit.js"].join("/")},{enable:!0,path:["aplus_cplugin",n,"monitor.js"].join("/")},{enable:_(),path:["aplus_cplugin",n,"track_deb.js"].join("/")},{enable:m(),path:["aplus_plugin_lazada","lazadalog.js"].join("/")},{enable:y(),path:["aplus_cplugin",n,"aplus_ws.js"].join("/")}]},n.getPlugins=function(e){var t="s/"+e.version+"/plugin",n=goldlog.aplus_cplugin_ver;return[{enable:f(e),path:[t,"aplus_urchin2.js"].join("/")},{enable:v(e),path:"aplus_plugin_guide/index.js"},{enable:h(e),path:["aplus_cplugin",n,"aol.js"].join("/")},{enable:d(e),path:[t,"aplus_spmact.js"].join("/")}]}},{"./util":8,"@ali/grey-publish":2}],8:[function(e,t,n){t.exports=e(1)},{"@ali/grey-publish":2}],9:[function(e,t,n){"use strict";var r,a=e("./plugins"),o=document;try{r=o.getElementById("beacon-aplus")||o.getElementById("tb-beacon-aplus")}catch(i){}var u=function(e){var t=[];try{if(r){var n=r.getAttribute(e||t);t=n.split(",")}}catch(a){t=[]}finally{return t}},s=function(e){var t=[];if(e)for(var n=0;n<e.length;n++){var r=e[n].enable,a=e[n].path;r===!0?t.push(a):"function"==typeof r&&r()&&t.push(a)}return t};n.getPlugins=function(e){var t=a.getPlugins(e);return[].concat(s(t),u("plugins"))},n.getFrontPlugins=function(e){var t=a.getFrontPlugins(e);return[].concat(s(t),u("frontPlugins"))}},{"./plugins":7}]},{},[5]);