(()=>{var e,t={65353:function(){var e=this&&this.__read||function(e,t){var r="function"==typeof Symbol&&e[Symbol.iterator];if(!r)return e;var n,o,a=r.call(e),i=[];try{for(;(void 0===t||t-- >0)&&!(n=a.next()).done;)i.push(n.value)}catch(e){o={error:e}}finally{try{n&&!n.done&&(r=a.return)&&r.call(a)}finally{if(o)throw o.error}}return i},t=this&&this.__spreadArray||function(e,t){for(var r=0,n=t.length,o=e.length;r<n;r++,o++)e[o]=t[r];return e};window.LockUnlockAction=function(r,n){var o=document.querySelectorAll("[data-locking-action]");t([],e(o)).forEach((function(e){e.addEventListener("click",(function(t){t.preventDefault(),t.stopPropagation();var o=document.createElement("form");o.action=e.dataset.lockingAction,o.method="POST";var a=document.createElement("input");if(a.type="hidden",a.name="csrfmiddlewaretoken",a.value=r,o.appendChild(a),void 0!==n){var i=document.createElement("input");i.type="hidden",i.name="next",i.value=n,o.appendChild(i)}document.body.appendChild(o),o.submit()}),{capture:!0})}))}}},r={};function n(e){var o=r[e];if(void 0!==o)return o.exports;var a=r[e]={id:e,loaded:!1,exports:{}};return t[e].call(a.exports,a,a.exports,n),a.loaded=!0,a.exports}n.m=t,e=[],n.O=(t,r,o,a)=>{if(!r){var i=1/0;for(c=0;c<e.length;c++){for(var[r,o,a]=e[c],l=!0,d=0;d<r.length;d++)(!1&a||i>=a)&&Object.keys(n.O).every((e=>n.O[e](r[d])))?r.splice(d--,1):(l=!1,a<i&&(i=a));l&&(e.splice(c--,1),t=o())}return t}a=a||0;for(var c=e.length;c>0&&e[c-1][2]>a;c--)e[c]=e[c-1];e[c]=[r,o,a]},n.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return n.d(t,{a:t}),t},n.d=(e,t)=>{for(var r in t)n.o(t,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},n.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),n.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),n.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),n.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.j=668,(()=>{var e={668:0};n.O.j=t=>0===e[t];var t=(t,r)=>{var o,a,[i,l,d]=r,c=0;for(o in l)n.o(l,o)&&(n.m[o]=l[o]);if(d)var u=d(n);for(t&&t(r);c<i.length;c++)a=i[c],n.o(e,a)&&e[a]&&e[a][0](),e[i[c]]=0;return n.O(u)},r=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})(),n.O(void 0,[751],(()=>n(65353)));var o=n.O(void 0,[751],(()=>n(90971)));o=n.O(o)})();
//# sourceMappingURL=lock-unlock-action.js.049fc1bf0bfd.map