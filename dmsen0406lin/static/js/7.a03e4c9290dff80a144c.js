webpackJsonp([7],{HXef:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n={name:"Home",components:{"p-footer":a("mzkE").a},data:function(){return{value2:!1,value1:!1,modal6:!1,loading:!0,isjcok1:!0,isjcok2:!1,message:"检查中...",switch1:!1,pStyle:{fontSize:"16px",color:"rgba(0,0,0,0.85)",lineHeight:"24px",display:"block",marginBottom:"16px"}}},methods:{asyncOK:function(){var t=this;setTimeout(function(){t.isjcok1=!1,t.isjcok2=!0},100),setTimeout(function(){t.message="已经为最新版本"},2500),setTimeout(function(){t.modal6=!1},4e3),setTimeout(function(){t.message="点击确定开始检查"},4500)},change:function(t){this.$Message.info("开关状态："+t)},swithon:function(t){this.$Message.info("功能："+t+" 开启")},swithdown:function(t){this.$Message.info("功能："+t+" 关闭")}}},o={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("Row",[a("Col",{staticStyle:{width:"342px"},attrs:{xs:{span:20,offset:1},sm:{span:8,offset:8},md:{span:8,offset:8},lg:{span:8,offset:8}}},[a("Card",{staticClass:"main"},[a("div",{staticStyle:{height:"auto"},attrs:{slot:"title"},slot:"title"},[a("Row",[a("Col",{attrs:{span:"8"}},[a("div",{staticStyle:{width:"auto"}},[a("img",{staticStyle:{width:"70%"},attrs:{src:"static/img/tou01.png",alt:""}})])]),t._v(" "),a("Col",{attrs:{span:"14",offset:2}},[a("Input",{staticStyle:{width:"auto","margin-bottom":"20px"},attrs:{id:"name",prefix:"ios-contact",placeholder:"name",disabled:"true"}}),t._v(" "),a("Input",{staticStyle:{width:"auto","margin-bottom":"20px"},attrs:{prefix:"md-grid",placeholder:"id",disabled:"true"}})],1)],1)],1),t._v(" "),a("Button",{staticStyle:{"margin-bottom":"20px",padding:"10px","font-family":"黑体"},attrs:{long:"",type:"primary"},on:{click:function(e){t.value1=!0}}},[t._v("个人信息")]),t._v(" "),a("Drawer",{attrs:{closable:!1,width:"70%"},model:{value:t.value1,callback:function(e){t.value1=e},expression:"value1"}},[a("p",{style:t.pStyle},[t._v("个人信息")]),t._v(" "),a("p",{style:t.pStyle},[t._v("基本信息")]),t._v(" "),a("div",{staticClass:"demo-drawer-profile"},[a("Row",[a("Col",{attrs:{span:"12"}},[t._v("\n             用户名: Aresn\n            ")]),t._v(" "),a("Col",{attrs:{span:"12"}},[t._v("\n              id: xxx\n            ")])],1),t._v(" "),a("Row",[a("Col",{attrs:{span:"12"}},[t._v("\n              城市: BeiJing\n            ")]),t._v(" "),a("Col",{attrs:{span:"12"}},[t._v("\n              国家: China\n            ")])],1),t._v(" "),a("Row",[a("Col",{attrs:{span:"12"}},[t._v("\n              生日: May 14, 1991\n            ")]),t._v(" "),a("Col",{attrs:{span:"12"}},[t._v("\n             邮箱: qq.com\n            ")])],1),t._v("\n          Message: Hello, 用户名\n        ")],1),t._v(" "),a("Divider")],1),t._v(" "),a("Button",{staticStyle:{"margin-bottom":"20px",padding:"10px","font-family":"黑体"},attrs:{long:"",type:"primary"},on:{click:function(e){t.value2=!0}}},[t._v("设置")]),t._v(" "),a("Drawer",{staticStyle:{"font-family":"华文行楷"},attrs:{title:"设置：",closable:!1},model:{value:t.value2,callback:function(e){t.value2=e},expression:"value2"}},t._l(6,function(e,n){return a("div",{staticStyle:{"margin-top":"15px"}},[a("span",{staticStyle:{"font-family":"楷体","font-size":"16px"}},[t._v("功能"+t._s(n)+"：")]),t._v(" "),a("Button",{staticStyle:{"margin-left":"5px","font-size":"16px"},attrs:{type:"success"},on:{click:function(e){t.swithon(n)}}},[t._v("开启\n        ")]),t._v(" "),a("Button",{staticStyle:{"margin-left":"5px","font-size":"16px"},attrs:{type:"error"},on:{click:function(e){t.swithdown(n)}}},[t._v("关闭")])],1)})),t._v(" "),a("Button",{staticStyle:{"margin-bottom":"20px",padding:"10px","font-family":"黑体"},attrs:{long:"",type:"primary"},on:{click:function(e){t.modal6=!0}}},[t._v("检查更新")]),t._v(" "),a("Modal",{attrs:{title:"检查更新",loading:t.loading},on:{"on-ok":t.asyncOK},model:{value:t.modal6,callback:function(e){t.modal6=e},expression:"modal6"}},[a("p",{directives:[{name:"show",rawName:"v-show",value:t.isjcok1,expression:"isjcok1"}]},[t._v("点击确定开始检查")]),t._v(" "),a("p",{directives:[{name:"show",rawName:"v-show",value:t.isjcok2,expression:"isjcok2"}]},[t._v(t._s(t.message))])]),t._v(" "),a("p-footer")],1)],1)],1)},staticRenderFns:[]};var s=a("VU/8")(n,o,!1,function(t){a("Qxi8")},null,null);e.default=s.exports},Qxi8:function(t,e){}});
//# sourceMappingURL=7.a03e4c9290dff80a144c.js.map