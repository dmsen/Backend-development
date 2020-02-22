$(document).ready(function(){
	$('.J_pcNav li').hover(function(){
		$(this).find(".navClass").show();
	},function(){
		$(this).find(".navClass").hide();
	});
	var base=true;
	var doUrl = $(".footer").attr('doUrl');
	//首页一行notice
	$("#home_default_notice").html($("#menu_notice span[name=home]").html());
	var name = $(".nav-collapse").attr('active');
	$("li[name="+name+"]",".nav").addClass('nav-active nav-b');
	// 顶部导航
	$('.nav_li').hover(function(){
		$('.nav_li').removeClass('nav-b');
		$('.nav_li').removeClass('current');		
		$(this).addClass('current');
		var mav_menu = $(this).find('.nav-menu');
		if(!mav_menu.find('.small').html()) {
			var name = $(this).attr('name');
			var notice = $("#menu_notice span[name="+name+"]").html();
			mav_menu.find('.small').html(notice);
		}
		mav_menu.show();
	},function(){
		$('.nav-active').addClass('nav-b');
		$('.nav_li').removeClass('current');		
		$(this).find('.nav-menu').hide();
	});

	$('.has_hover_bar').hover(function(){
		$('.nav_li').removeClass('nav-b');
		$('.nav_li').removeClass('current');		
		$(this).next().addClass('current');
		$(this).next().find('.nav-menu').show();
	},function(){
		$('.nav-active').addClass('nav-b');
		$('.nav_li').removeClass('current');		
		$(this).next().find('.nav-menu').hide();
	});
	
	/*下载更新下载量*/
	$("#docurl").click(function(){
		var obj = $(this);
		var aid = obj.attr('aid');
		if(!aid) return false;
		var sm = parseInt(obj.parent().find(".sum").text());
		$.ajax({
			url : '/api/cms_list.php',
			type : 'post',
			data : {ctype:'downs', article_id:aid},
			timeout : 20000,
			dataType : 'json',
			error : function(m){
				//console.log('请求有误，请刷新后重试!');
			},
			success : function(msg){
				if(!msg['status']){
					//console.log(msg['msg']);
				}
			}
		});
	});

	/*顶踩赞*/
	$("#onFavors").click(function(){
		var obj = $(this);
		var aid = obj.attr('aid');
		if(!aid) return false;
		var sm = parseInt(obj.parent().find(".sum").text());
		$.ajax({
			url : '/api/cms_list.php',
			type : 'post',
			data : {ctype:'favors', article_id:aid},
			timeout : 20000,
			dataType : 'json',
			error : function(m){
				//console.log('请求有误，请刷新后重试!');
			},
			success : function(msg){
				if(!!msg['status']){
					if(msg['msg'] == '1') {
						obj.find(".zan-btna").css('background-position','0 -181px');
						obj.parent().find(".sum").text(sm+1);
					}
					else {
						obj.find(".zan-btna").css('background-position','0 -163px');
						obj.parent().find(".sum").text(sm-1);
					}
				}
				else {
				   //console.log(msg['msg']);
				}
			}
		});
	});

	//搜索
	var kw = $("#keyword");
	$(".search-btn").click(function(){		
		if(!kw.val()) {
			kw.parent().css('border', '1px red solid');
			return false;
		}
		var kwd = rawurlencode(kw.val());
		location.href = '/?m-cms-q-search-keyword-'+kwd+'.html';
	});
	function enterSearch(e) {
		var kw = $("#keyword");
		if(e && e.keyCode==13){
			if(!kw.val()) {
				kw.parent().css('border', '1px red solid');
				return false;
			}
			var kwd = rawurlencode(kw.val());
			location.href = '/?m-cms-q-search-keyword-'+kwd+'.html';
		}
	}
	//滚动
	$('.toUp').click(sideScroll);
	$('.toDown').click(sideScroll);
	
	var sideScrollAt = 1;
	
	function sideScroll(e) {
		var e = e || window.event, 
			target = $(e.target),
			$ul = $("#shalong_list"),
			len = $ul.find(".font_list_con").length - 1,
			sign = '';
		
		$('.toDown_box, .up-down, .toUp_box').hide();
		
		if (target.hasClass("toDown")) {
			sign = '-';
			(++sideScrollAt >= len / 3) ? $('.toUp_box').show() : $('.up-down').show();
		} else {
			sign = '+';
			(--sideScrollAt <= 1) ? $('.toDown_box').show() : $('.up-down').show();
		}
		$ul.animate({top: sign + '=335px'}, 400);
	}
	
	$('.toDown2').on('click',function(){
		$('.hotspot-box').css({'height':'100%','overflow':'visible'});
		$(this).hide();
	});
	// 焦点图
	(function(){
		var timer=null;
		var now=0;
		var aTab=$('.tab_focus');
		for(var i=0;i<aTab.length;i++){
			tabFocus(aTab[i]);
		}
		function tabFocus(obj){
			var oUl=$('.tab_list',obj);
			//	oUl[0].innerHTML+=oUl[0].innerHTML;
			var aLi=$('.tab_list .list_li');
			var aTxt=$('.tab_list .font_li');
			if(typeof(aLi[0]) != 'undefined')
			var l=aLi[0].offsetWidth;
			oUl.css({'width':l*$('.tab_list .list_li').length});
			var base=true;
			var aBtn=$('.btn_nmb');
			var aFont_li=$('.font_li');
			var index = 0;
			//$('.list_ul').css('width',l*aFont_li.length+'px');
			//for(var i=0;i<aBtn.length;i++)aBtn[i].index=i;
			aBtn.each(function(i){
				$(this).attr('txt_id',i);
			});
			$('.btn_nmb').hover(function(){
				//clearInterval(timer);
				//console.log(this.index);
				index = parseInt($(this).attr('txt_id'));
				//oUl.css('left',-1*l*index);
				base=false;
				oUl.stop().animate({'left':-1*l*index},{
					duration: 900,
					easing:"easeOutQuart",
					complete: function(){
						base=true;
					}
				});
				/*
				now=this.index;
				if(base==false)return;
				base=false;
				oUl.stop().animate({'left':-l*(now)+'px'},{
					duration: 900,
					easing:"easeOutQuart",
					complete: function(){
						base=true;
					}
				});
*/
				$('.btn_nmb',obj).removeClass('active');
				$(this).addClass('active');

			},function(){});
			timer=setInterval(function(){
				++index;
				if(index==aLi.length){
					index=0;
				}
				var width = parseInt(l);
				$('.btn_nmb',obj).removeClass('active');
				$($('.btn_nmb')[index]).addClass('active');
				oUl.stop().animate({'left':-width*index},{
						duration: 900,
						easing:"easeOutQuart",
						complete: function(){
							base=true;

						}
				});
			},4000);
		/*
			for(var i=0;i<aLi.length;i++){
				aLi[i].index=i;
			}
			*/
		//	console.log(aLi.length)
		//	aTxt.hover(function(){
		//		$(this).find('h3').css('color',"#bc0000");
		//		$(this).find('p').css('color',"#151515");
		//	},
		//	function(){
		//		$(this).find('h3').css('color',"#151515");
		//		$(this).find('p').css('color',"#666");
		//	});
			/*
			$('.font_li').on('mouseover',function(){
				$('h3',$(this)).css('color','#bc0000');
			});
			$('.font_li').on('mouseout',function(){
				$('h3',$(this)).css('color','#151515');
			});
			*/
		}
		
	})();
	
	if($('.navbar-form .span3')[0]){
		$('.navbar-form .span3')[0].onclick=function(ev){
			oEvent=ev||event;
				oEvent.cancelBubble=true;  
			$('.search-btn span',$(this).parent()).css({'backgroundPosition':'10px -27px'})
			
		};
	}

	$(document).on('click',function(){	
		$('.search-btn span').css({'backgroundPosition':'10px 5px'});

		$('.code').hide();
		$('.feedbackBox').hide();
		$('.eweiImg').hide();
	});

	//侧导航各按钮显隐
	show('.ewei','.eweiImg');
	show('.code-btn','.code','.feedbackBox');
	//show('.btn-toolHelp','.feedbackBox','.code');
	$(".btn-toolHelp").click(function(){
		window.open('/Blog/Article/detail/id/20116.html');
	});
	if(typeof($('.feedbackBox')[0]) !== 'undefined') {
		$('.feedbackBox')[0].onclick=function(ev){

				oEvent=ev||event;
				oEvent.cancelBubble=true;  
		}
	}
	function show(btn,obj,obj2){
		if(typeof($(btn)[0]) == 'undefined') return;
		$(btn)[0].onclick=function(ev){

			oEvent=ev||event;
			oEvent.cancelBubble=true;
			if(btn == '.ewei') {
				$(obj).css({'top':oEvent.pageY-172,'left':oEvent.pageX-9});
			}
			if($(obj)[0].style.display=='none'){
				$(obj).show();
			}else{
				$(obj).hide();
			}
			$(obj2).hide();
		}
	}
	
	
	//分类
	$("#ccid_choose a").click(function(){
		var ccid = $(this).attr('ccid');
		if(!ccid) return false;
		$.post("/api/cms_list.php",{ctype:'list_url', ccid:ccid},function(result){
			location.href='/?'+result;
		});
	});
	$("#eid_choose a").click(function(){
		var eid = $(this).attr('eid');
		if(!eid) return false;
		$.post("/api/cms_list.php",{ctype:'list_url', eid:eid},function(result){
			location.href='/?'+result;
		});
	});
	$("#year_choose a").click(function(){
		var year = $(this).text();
		if(!year) return false;
		$.post("/api/cms_list.php",{ctype:'list_url', year:year},function(result){
			location.href='/?'+result;
		});
	});
	//删除选项
	$(".j-sortSowa").click(function(){
		var is_remove = $(this).attr('type');
		$.post("/api/cms_list.php",{ctype:'list_url', is_remove:is_remove},function(result){
			location.href='/?'+result;
		});
	});
	//清除筛选
	$(".j-sortRemove").click(function(){
		var cid = $(this).attr('cid');
		location.href="/?m-cms-q-list-cid-"+cid+".html";
	});
	var aHotSpot=$('.a-title');
//	console.log(aHotSpot.length)
	for(var i=0;i<aHotSpot.length;i++){
		aHotSpot[i].index=i;
	}

	for(var i=0;i<$('.j-hotspotA a').length;i++){
		$('.j-hotspotA a')[i].index=i;
	}

	for(var i=0;i<$('.hover_p').length;i++){
		$('.hover_p')[i].index=i;
	}
	//console.log(aHotSpot.length)
// 今日热文交互
	aHotSpot.on('mouseover',function(){
		$(this).css('color','#bc0000');
		$($('.j-hotspotA a')[this.index]).css('color','#151515');
		$($('.j-hotspotA em')[this.index]).css('backgroundPosition','0 -127px');
		if($('.hover_p')){
			$($('.hover_p')[this.index]).css('color','#151515');
		}
	});
	aHotSpot.on('mouseout',function(){
		$(this).css('color','#151515');
		$('.j-hotspotA a').css('color','#666');
		$('.j-hotspotA em').css('backgroundPosition','0 -112px');
		if($('.hover_p')){
			$($('.hover_p')[this.index]).css('color','#666');
		}

	});
	$('.j-hotspotA a').on('mouseover',function(){
		$(this).css('color','#151515');
		$(aHotSpot[this.index]).css('color','#bc0000');
		$($('.j-hotspotA em')[this.index]).css('backgroundPosition','0 -127px');
	});
	$('.j-hotspotA a').on('mouseout',function(){
		$(this).css('color','#666');
		$(aHotSpot[this.index]).css('color','#151515');
		$('.j-hotspotA em').css('backgroundPosition','0 -112px');
	});
	$('.hover_p').on('mouseover',function(){
		$(this).css('color','#151515');
		$(aHotSpot[this.index]).css('color','#bc0000');
	});
	$('.hover_p').on('mouseout',function(){
		$(this).css('color','#666');
		$(aHotSpot[this.index]).css('color','#151515');
	});
	

	$('.time-classify .the_more').on('click',function(){
		this.base=!this.base;
		//console.log(this.base);
		if(this.base){
			$(this).addClass('j-theMoreup');
			$('.time-classify .the_more a').html('收起');
			$('.classify-ul',$(this).parent()).css('height','100%');
		}else{
			$(this).removeClass('j-theMoreup');
			$('.time-classify .the_more a').html('更多');
			$('.classify-ul',$(this).parent()).css('height','35px');
		}
		
	})
	// 
	$('.j-spetopic').on('mouseover',function(){
		$('.j-sort',$(this)).css('background','#81a1b8');
	});
	$('.j-spetopic').on('mouseout',function(){
		$('.j-sort',$(this)).css('background','#9fbed3');
	});
	// 内容展开
	$('.j-hotList li').on('mouseover',function(){
		$('.j-hotList p').hide();
		$('p',$(this)).show();
			
	});
	//分页显隐
	var more=true;
	$('.w-moredown').on('click',function(){
		if(more){
			$('.d-moredowDiv').show();
		}else{
			$('.d-moredowDiv').hide();
		}
		more=!more;
	});
	//留言板
	var oMessBox=$('.j-leave ul');
	var oText=$('.text-box');
	oText.on('click',function(){
		oText[0].value='';
	});
	
	$('.messBtn').on('click',function(){
		var oLi=document.createElement('li');
		oLi.className='clearfix mess-list';
		oLi.innerHTML='<div class="avatar"><img src="/html/static/img/ewmaImg.png" width="48" height="48"></div>'+
                        '<div class="info">'+
                        	'<p class="anther"><em class="mr20">我爱音乐</em>'+'t1+t2'+' </p>'+
                            '<p>'+oText[0].value+'</p>'+
                            '<p class="zanBox" ><a href="#" class="c-red mr10">回复</a><em class="mr10">|</em><a href="#" class="c-red"><em class="zan-btna"></em>赞</a></p>'+
                        '</div>';
        var aLi=$('.mess-list');

        if(aLi.length==0){
       		oMessBox.append($(oLi));
        }
      	else if(aLi.length>0){
        	oMessBox[0].insertBefore(oLi,aLi[0]);
        }
        oText[0].value='';      
	});
	   function toDou(s){
	      if(s<10){
	         return '0'+s;
	       }else{
	        return s;
	       }
	   }


	// 	侧导航
	
	 $(window).scroll(function(){
		if ($(window).scrollTop()>300)
			$(".toolTop").fadeIn(500);
		else
			$(".toolTop").fadeOut(400);
	});		
	$(".toolTop").click(function(){
		$('body,html').animate({scrollTop:0},400);
	});

	//弹窗
	var bodyH=document.body.scrollHeight;
	$('.login').on('click',function(){
		$('#popOverplay').show();
		$('.pop_reg').hide();
		$('.pop_login').show(150);

	});
	$('.reg').on('click',function(){
		$('#popOverplay').show();
		$('.pop_login').hide();
		$('.pop_reg').show(120);

	});
	$('.popClose').on('click',function(){
		$('#popOverplay').hide();
		$('.popBox').hide();
	});

	//页面首页加载内容！important
	if($("#body_name").attr('value') == 'index') {
		//loadArticles(3837,'focus_txt_one', 1);
		//setTimeout(function(){loadArticles(3904, 'focus_txt_two', 1)},200);
		//setTimeout(function(){loadArticles(3827, 'focus_txt_three', 1)},400);
		//setTimeout(function(){loadArticles('top_goods', 2, 2592000,0)},800);
		//setTimeout(function(){loadShaLongArticles(4033)},50);
	}
	function loadArticles(tag_id,show_id, num) {
		$.ajax({
			url : '/blog/index/lists/tag/'+tag_id+'.html',
			type : 'post',
			data : {display:'json'},
			timeout : 30000,
			dataType : 'json',
			error : function(m){
				//console.log('请求有误，请刷新后重试!');
			},
			success : function(data){
				var html = [];
				if(data.info != null) {
					var msg = data.info;
					for (var i in msg) {
						if(i == num) {
							break;
						}
						var subject = msg[i]["title"];
						//html.push('<a class="j-sjublock pic1 alinkhover" target="_blank" href="/blog/article/detail/id/' +  msg[i]["id"]+'.html">');
						html.push('<a class="j-sjublock pic1 alinkhover" target="_blank" href="/blog/article/detail/id/' +  msg[i]["id"]+'.html"><h3 class="h3" style="height:38px;overflow:hidden" title="' + subject + '">' + subject + '</h3><p style="font-size:13px">' + msg[i]["description"] + '</p></a>');						
						html.push('<span style="float:right"><a href="/blog/index/lists/tag/' +tag_id+'.html" target="_blank">更多</a></span>');
					}
				}

				$("#"+show_id).html(html);
			}
		});
	}

	//function loadShaLongArticles(tag_id, num) {
	//	tag_id = !!tag_id?tag_id:'4033';
	//	num = !!num>0?num:10;
	//	$.ajax({
	//		url : '/blog/index/lists/tag/'+tag_id+'.html',
	//		type : 'get',
	//		data : {display:'json'},
	//		timeout : 10000,
	//		dataType : 'json',
	//		error : function(m){
	//			//console.log(tag_id + '数据加载有误，可尝试刷新!');
	//		},
	//		success : function(data){
	//			var html = [];
	//			if(data.info != null) {
	//				var msg = data.info;
	//				for (var i in msg) {
	//					if(i > num) {
	//						break;
	//					}
	//					var subject = msg[i]["title"];
	//					html.push('<li class="font_list_con">');
	//					html.push(	'<a class="alinkhover" target="_blank" href="/blog/article/detail/id/' +  msg[i]["id"]+'.html">');
	//					html.push(		'<h3 class="h3" title="' + subject + '">' + subject + '</h3>');
	//					html.push(		'<p>' + msg[i]["description"] + '</p>');
	//					html.push(	'</a>');
	//					html.push('</li>');
	//				}
	//			}
	//			$("#shalong_list").html(html.join(''));
	//		}
	//	});
	//}

});

//验证码
function changeVerify() {
	// var url = '/yck.php?t='+Math.ceil(Math.random()*10000);
	// $(".verify_code img").attr('src', url);
}

function rawurlencode(str) {
	str = (str + '').toString();
	return encodeURIComponent(str).replace(/!/g, '%21').replace(/'/g, '%27').replace(/\(/g, '%28').replace(/\)/g, '%29').replace(/\*/g, '%2A');
}
