"use strict";(self.webpackChunkimio_smartweb_core_webcomponents=self.webpackChunkimio_smartweb_core_webcomponents||[]).push([[792],{3991:function(e,t,r){r(8709);t.Z=r.p+"assets/location-active-bla.fe8acf1aaf227a942ff7feed87fa2d22.svg"},7518:function(e,t,r){r(8709);t.Z=r.p+"assets/location-bla.1423bcce16ddcb21141430cac1428dc1.svg"},3792:function(e,t,r){r.r(t),r.d(t,{default:function(){return I}});var n=r(8709),a=r(2707),l=r(5110),c=r(804);function o(){return o=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e},o.apply(this,arguments)}var i=function(e){return n.createElement(c.ZP,o({speed:2,viewBox:"0 0 710.04 150",backgroundColor:"#f3f3f3",foregroundColor:"#ecebeb",className:"skeleton"},e),n.createElement("rect",{className:"cls-1",width:"246",height:"150"}),n.createElement("rect",{className:"cls-1",x:"275.74",width:"225.04",height:"18.87"}),n.createElement("rect",{className:"cls-1",x:"275.74",y:"47.43",width:"434.3",height:"10.19"}),n.createElement("rect",{className:"cls-1",x:"275.74",y:"78.06",width:"434.3",height:"10.19"}))},u=r(7749),s=r(4844);function m(e){return m="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e},m(e)}function f(e,t){if(null==e)return{};var r,n,a=function(e,t){if(null==e)return{};var r,n,a={},l=Object.keys(e);for(n=0;n<l.length;n++)r=l[n],t.indexOf(r)>=0||(a[r]=e[r]);return a}(e,t);if(Object.getOwnPropertySymbols){var l=Object.getOwnPropertySymbols(e);for(n=0;n<l.length;n++)r=l[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(a[r]=e[r])}return a}function p(e){var t=function(e,t){if("object"!==m(e)||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var n=r.call(e,t||"default");if("object"!==m(n))return n;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"===m(t)?t:String(t)}function y(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function b(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?y(Object(r),!0).forEach((function(t){v(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):y(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function v(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function d(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==r)return;var n,a,l=[],c=!0,o=!1;try{for(r=r.call(e);!(c=(n=r.next()).done)&&(l.push(n.value),!t||l.length!==t);c=!0);}catch(e){o=!0,a=e}finally{try{c||null==r.return||r.return()}finally{if(o)throw a}}return l}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return h(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return h(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function h(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}var g=function(e){var t=d((0,n.useState)({}),2),r=t[0],a=t[1],l=d((0,n.useState)(null),2),c=l[0],o=l[1],i=d((0,n.useState)(null),2),m=i[0],y=i[1],h=(0,s.Z)({method:"get",url:"",baseURL:e.url,headers:{Accept:"application/json"},params:""}),g=h.response;h.error,h.isLoading,(0,n.useEffect)((function(){if(null!==g){var e=g.topics.map((function(e){return{value:e.token,label:e.title}})),t=g.taxonomy_contact_category?g.taxonomy_contact_category.map((function(e){return{value:e.token,label:e.title}})):"";o(e),y(t)}}),[g]);var E=(0,n.useCallback)((function(e){var t=e.target,r=t.name,n=t.value;return a((function(e){return b(b({},e),{},v({},r,n))}),[])})),w=(0,n.useCallback)((function(e,t){var r=t.name;e?a((function(t){return b(b({},t),{},v({},r,e.value))}),[]):a((function(e){var t=b({},e);t[r];return f(t,[r].map(p))}))}));return(0,n.useEffect)((function(){e.onChange(r)}),[r]),n.createElement("div",null,n.createElement("form",{onSubmit:function(t){t.preventDefault(),e.onChange(r)}},n.createElement("label",null,"Recherche",n.createElement("input",{name:"search",type:"text",value:r.search,onChange:E})),n.createElement("button",{type:"submit"},"Do the thing")),n.createElement("div",{className:"r-filter  facilities-Filter"},n.createElement("span",null,"Catégories"),n.createElement(u.ZP,{name:"taxonomy_contact_category",className:"select-custom-class library-facilities",isClearable:!0,onChange:w,options:m&&m,placeholder:"Toutes"})),n.createElement("div",{className:"r-filter topics-Filter"},n.createElement("span",null,"Thématiques"),n.createElement(u.ZP,{name:"topics",className:"select-custom-class library-topics",isClearable:!0,onChange:w,options:c&&c,placeholder:"Toutes"})))};function E(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==r)return;var n,a,l=[],c=!0,o=!1;try{for(r=r.call(e);!(c=(n=r.next()).done)&&(l.push(n.value),!t||l.length!==t);c=!0);}catch(e){o=!0,a=e}finally{try{c||null==r.return||r.return()}finally{if(o)throw a}}return l}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return w(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return w(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function w(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}var O=function(e){var t=e.contactArray,r=e.onChange,a=(0,l.k6)(),c=(0,l.UO)().id,o=E((0,n.useState)({}),2),i=o[0],u=o[1];return(0,n.useEffect)((function(){if(t.length>0){var e=t.filter((function(e){return e.UID===c}));u(e[0])}}),[c,t]),n.createElement("div",{className:"contact-content"},n.createElement("button",{type:"button",onClick:function(){a.push("."),r(null)}},"Go home"),n.createElement("div",{className:"contactCard"},n.createElement("div",{className:"contactText"},n.createElement("div",{className:"contactTextTitle"},n.createElement("span",{className:"title"},i.title)),n.createElement("div",{className:"contactTextAll"},i.category?n.createElement("span",null,i.category):"",n.createElement("div",{className:"adresse"},i.number?n.createElement("span",null,i.number+" "):"",i.street?n.createElement("span",null,i.street+", "):"",i.complement?n.createElement("span",null,i.complement+", "):"",i.zipcode?n.createElement("span",null,i.zipcode+" "):"",i.city?n.createElement("span",null,i.city):""),n.createElement("div",{className:"itineraty"},i.street?n.createElement("a",{href:"https://www.google.com/maps/dir/?api=1&destination="+i.street+"+"+i.number+"+"+i.complement+"+"+i.zipcode+"+"+i.city+"+"+i.country},"Itinéraire"):""),n.createElement("div",{className:"phones"},i.phones?i.phones.map((function(e){return n.createElement("span",null,e.number)})):""),n.createElement("div",{className:"mails"},i.mails?i.mails.map((function(e){return n.createElement("span",null,e.mail_address)})):""),n.createElement("div",{className:"topics"},i.topics?i.topics.map((function(e){return n.createElement("span",null,e.title)})):"")))))},j=r(4570),S=function(e){var t=e.contactItem,r=t.title&&t.title,a=t.taxonomy_contact_category?t.taxonomy_contact_category[0].title:"",l=t.number?t.number:"",c=t.street?t.street:"",o=t.complement?t.complement:"",i=t.zipcode?t.zipcode:"",u=t.city?t.city:"",s=(t.country&&t.country,t.phones?t.phones:""),m=t.mails?t.mails:"",f=t.topics?t.topics:"";return n.createElement("div",{className:"r-list-item"},n.createElement("div",{className:"r-item-img",style:{backgroundImage:t.image?"url("+t.image.scales.preview.download+")":"url("+j.Z+")"}}),n.createElement("div",{className:"r-item-text"},n.createElement("span",{className:"r-item-title"},r),a?n.createElement("span",{className:"r-item-categorie"},a):"",n.createElement("div",{className:"r-item-all"},n.createElement("div",{className:"r-item-adresse"},l?n.createElement("span",null,l+" "):"",c?n.createElement("span",null,c+", "):"",o?n.createElement("span",null,o+", "):"",n.createElement("br",null),i?n.createElement("span",null,i+" "):"",u?n.createElement("span",null,u):""),n.createElement("div",{className:"r-item-contact"},n.createElement("div",{className:"phones"},s?s.map((function(e,t){return n.createElement("span",{key:t},e.number)})):""),n.createElement("div",{className:"mails"},m?m.map((function(e,t){return n.createElement("span",{key:t},e.mail_address)})):""),n.createElement("div",{className:"topics"},f?f.map((function(e,t){return n.createElement("span",{key:t},e.title)})):"")))))},N=function(e){var t=e.contactArray,r=e.onChange,l=e.parentCallback;return n.createElement(n.Fragment,null,n.createElement("ul",{className:"r-result-list annuaire-result-list"},t.map((function(e,t){return n.createElement("li",{key:t,className:"r-list-item-group",onClick:function(){return t=e.UID,void r(t);var t}},n.createElement(a.rU,{className:"r-list-item-link",style:{textDecoration:"none"},to:{pathname:"".concat(e.UID),state:{idItem:e.UID}}}),n.createElement(S,{contactItem:e,key:e.created}))}))),n.createElement("button",{onClick:function(e){l()}},"Click me"))};r(8818),r(7518),r(3991);function A(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function C(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?A(Object(r),!0).forEach((function(t){k(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):A(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function k(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function P(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==r)return;var n,a,l=[],c=!0,o=!1;try{for(r=r.call(e);!(c=(n=r.next()).done)&&(l.push(n.value),!t||l.length!==t);c=!0);}catch(e){o=!0,a=e}finally{try{c||null==r.return||r.return()}finally{if(o)throw a}}return l}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return x(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return x(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function x(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}var I=function(e){var t=P((0,n.useState)([]),2),r=t[0],c=t[1],o=P((0,n.useState)(null),2),u=(o[0],o[1]),m=P((0,n.useState)({}),2),f=m[0],p=m[1],y=P((0,n.useState)({}),2),b=y[0],v=y[1],d=P((0,n.useState)(5),2),h=d[0],E=d[1],w=P((0,n.useState)(null),2),j=w[0],S=w[1],A=(0,s.Z)({method:"get",url:"",baseURL:"http://localhost:3000/Plone/actualites/@results",headers:{Accept:"application/json",ContentType:"application/json"},params:f},[f]),k=A.response,x=(A.error,A.isLoading);(0,n.useEffect)((function(){console.log(k.json()),null!==k&&c(k.json().items)}),[k]);var I=function(e){u(e)};return(0,n.useEffect)((function(){p(C(C({},b),{},{b_size:h,fullobjects:1}))}),[b,h]),console.log(r),n.createElement("div",{className:"ref",ref:function(e){e&&S(e.getBoundingClientRect().top)},style:{height:"calc(100vh -  ".concat(j,"px)")}},n.createElement(a.UT,null,n.createElement("div",{className:"r-wrapper r-annuaire-wrapper"},n.createElement("div",{className:"r-result r-annuaire-result"},n.createElement(l.rs,null,n.createElement(l.AW,{path:"/:id"},n.createElement(O,{onChange:I,contactArray:r})),n.createElement(l.AW,{exact:!0,path:"*"},n.createElement("div",{className:"r-result-filter annuaire-result-filter"},n.createElement(g,{url:e.queryFilterUrl,onChange:function(e){v(e)}})),x?n.createElement("div",null,n.createElement(i,null)," ",n.createElement(i,null)," ",n.createElement(i,null)):n.createElement(N,{onChange:I,contactArray:r,parentCallback:function(){E(h+5)}})))))))}},4844:function(e,t,r){var n=r(8709),a=r(1806),l=r.n(a);function c(e,t,r,n,a,l,c){try{var o=e[l](c),i=o.value}catch(e){return void r(e)}o.done?t(i):Promise.resolve(i).then(n,a)}function o(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=null==e?null:"undefined"!=typeof Symbol&&e[Symbol.iterator]||e["@@iterator"];if(null==r)return;var n,a,l=[],c=!0,o=!1;try{for(r=r.call(e);!(c=(n=r.next()).done)&&(l.push(n.value),!t||l.length!==t);c=!0);}catch(e){o=!0,a=e}finally{try{c||null==r.return||r.return()}finally{if(o)throw a}}return l}(e,t)||function(e,t){if(!e)return;if("string"==typeof e)return i(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);"Object"===r&&e.constructor&&(r=e.constructor.name);if("Map"===r||"Set"===r)return Array.from(e);if("Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r))return i(e,t)}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function i(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,n=new Array(t);r<t;r++)n[r]=e[r];return n}t.Z=function(e){var t=o((0,n.useState)(null),2),r=t[0],a=t[1],i=o((0,n.useState)(""),2),u=i[0],s=i[1],m=o((0,n.useState)(!0),2),f=m[0],p=m[1],y=function(){var e,t=(e=regeneratorRuntime.mark((function e(t){var r;return regeneratorRuntime.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return p(!0),e.prev=1,e.next=4,l().request(t);case 4:r=e.sent,a(r.data),s(null),e.next=12;break;case 9:e.prev=9,e.t0=e.catch(1),s(e.t0);case 12:return e.prev=12,p(!1),e.finish(12);case 15:case"end":return e.stop()}}),e,null,[[1,9,12,15]])})),function(){var t=this,r=arguments;return new Promise((function(n,a){var l=e.apply(t,r);function o(e){c(l,n,a,o,i,"next",e)}function i(e){c(l,n,a,o,i,"throw",e)}o(void 0)}))});return function(e){return t.apply(this,arguments)}}();return(0,n.useEffect)((function(){y(e)}),[e.params]),{response:r,error:u,isLoading:f}}},4570:function(e,t,r){t.Z=r.p+"assets/img-placeholder-bla.a2b8b384c46ce56c99f042dc4625d309.png"}}]);