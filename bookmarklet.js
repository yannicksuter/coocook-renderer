post('http://localhost:8080/snipped', {foo: 'bar'})

function post(url, formData) {
  const makeElem = (tag, props) => Object.assign(document.createElement(tag), props)
  const form = makeElem('form', { action: url, method: 'post', style: 'display: none' })
  for (const [name, value] of Object.entries(formData)) {
    form.appendChild(makeElem('input', { name, value }))
  }
  document.body.appendChild(form)
  form.submit()
}

function postSelectionHtml() {
    var html = "";
    if (typeof window.getSelection != "undefined") {
        var sel = window.getSelection();
        if (sel.rangeCount) {
            var container = document.createElement("div");
            for (var i = 0, len = sel.rangeCount; i < len; ++i) {
                container.appendChild(sel.getRangeAt(i).cloneContents());
            }
            html = container.innerHTML;
        }
    } else if (typeof document.selection != "undefined") {
        if (document.selection.type == "Text") {
            html = document.selection.createRange().htmlText;
        }
    }

	const makeElem = (tag, props) => Object.assign(document.createElement(tag), props)
	const form = makeElem('form', { action: 'http://localhost:8080/snipped', method: 'post', style: 'display: none' })
	for (const [name, value] of Object.entries({title: document.title, origin: window.location.href, content: html}})) {
		form.appendChild(makeElem('input', { name, value }))
	}
	document.body.appendChild(form)
	form.submit()
}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

javascript:(function(){var h="",s,g,c,i;if(window.getSelection){s=window.getSelection();if(s.rangeCount){c=document.createElement("div");for(i=0;i<s.rangeCount;++i){c.appendChild(s.getRangeAt(i).cloneContents());}h=c.innerHTML}}else if((s=document.selection)&&s.type=="Text"){h=s.createRange().htmlText;}post('http://localhost:8080/snipped', {title: document.title, origin: window.location.href, content: h})})();function post(a,b){const c=(e,f)=>Object.assign(document.createElement(e),f),d=c('form',{action:a,method:'post',style:'display: none'});for(const[e,f]of Object.entries(b))d.appendChild(c('input',{name:e,value:f}));document.body.appendChild(d),d.submit()}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

javascript:(function(){document.body.style.background = 'pink';})();

javascript:post('https://example.com',{foo:'bar'});function post(a,b){const c=(e,f)=>Object.assign(document.createElement(e),f),d=c('form',{action:a,method:'post',style:'display: none'});for(const[e,f]of Object.entries(b))d.appendChild(c('input',{name:e,value:f}));document.body.appendChild(d),d.submit()}