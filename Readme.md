DJango笔记
---
## CSRF
CSRF（Cross-site request forgery跨站请求伪造，也被称为“one click attack”或者session riding，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。尽管听起来像跨站脚本（XSS），但它与XSS非常不同，并且攻击方式几乎相左。XSS利用站点内的信任用户，而CSRF则通过伪装来自受信任用户的请求来利用受信任的网站。与XSS攻击相比，CSRF攻击往往不大流行（因此对其进行防范的资源也相当稀少）和难以防范，所以被认为比XSS更具危险性。

django自动加载防CSRF的中间件（默认）
	在settings.py 中开启
	```
		'django.middleware.common.CommonMiddleware',
	    'django.middleware.csrf.CsrfViewMiddleware',  <--这个
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	```

### CSRF只针对POST请求 所以为了更加安全，请在你的代码中加入判断
	```
		if request.method == "POST":
			#你的业务逻辑
	```


### 使用csrf保护你的视图
	```
		from django.views.decorators.csrf import requires_csrf_token,csrf_exempt,csrf_protect
		@requires_csrf_token		使用这个装饰器装饰的视图需要验证csrf token
		@csrf_exempt 				使用这个装饰器装饰的视图不需要验证csrf token，即使csrf中间件开启
		@csrf_protect 				使用这个装饰器装饰的视图需要验证csrf token，即使csrf中间件没有开启	
	```


### 自己应用的POST请求如何提交
	`django 会在你每个视图的response中夹杂一个包含csrf_token值的cookie`
  django会检查请求的头部和数据，头部中包含key为X-CSRFToken的CSRF_Token 或者 数据中含有{'csrfmiddlewaretoken':'CSRF_Token'}

#### Form 表单
	使用render渲染模板，将{% csrf_token %}放入要提交的表单中生成type='hide'的Input框

#### ajax
	```
				jQuery(document).ajaxSend(function(event, xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            function sameOrigin(url) {
                // url could be relative or scheme relative or absolute
                var host = document.location.host; // host + port
                var protocol = document.location.protocol;
                var sr_origin = '//' + host;
                var origin = protocol + sr_origin;
                // Allow absolute or scheme relative URLs to same origin
                return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                    // or any other URL that isn't scheme relative or absolute i.e relative.
                    !(/^(\/\/|http:|https:).*/.test(url));
            }
            function safeMethod(method) {
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
				<!-- xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken')); -->
                xhr.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');

            }
            });
	```

## session

### session 和 cookie的区别（https://www.zhihu.com/question/19786827）
	> session 将服务器和客户端交互的信息(也就是常说的跟踪会话)保存到服务器端(django将session存放在数据库中)，php写在硬盘上，常用于验证用户是否登录，session 是依赖于cookie的，因为session，需要在cookie中存放session id

	> cookie 是保存在客户端的，用于存放客户的一些临时信息到硬盘上

### django中设置session 过期时间(https://docs.djangoproject.com/en/1.11/topics/http/sessions/#using-sessions-in-views)
	另外一种方法:
		在settings.py中进行全局设定:
			```
			SESSION_COOKIE_AGE = 60 * 30 # 30分钟
			SESSION_SAVE_EVERY_REQUEST = False
			#每一次请求都会保存一次session 默认为False,默认的session保存机制是当session被修改时才保存
			SESSION_EXPIRE_AT_BROWSER_CLOSE = True # 关闭浏览器，则COOKIE失效
			```	

