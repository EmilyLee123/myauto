#config_element对应模块的所有的元素定位
config_element = {

    "cms_login":{
        #cms登录包含验证码登录
        "图标": ['xpath', '//*[@id="view-top"]/header/div[1]/h1/a/img'],
        "帮助": ['xpath', '//*[@id="view-top"]/header/div[2]/nav[3]/ol/li[1]/a'],
        "登录右": ['xpath', '//*[@id="view-top"]/header/div[2]/nav[3]/ol/li[2]/a'],
        "语言": ['xpath', '//*[@id="view-top"]/header/div[2]/nav[2]/div/ul/li[1]/a'],

        "标题": ['xpath', '//*[@id="content"]/div/section/header/h1'],

        "邮箱或手机": ['xpath', '//*[@id="field-email-or-mobile"]/label'],
        "账号输入框": ['id', 'email'],
        "密码": ['xpath', '//*[@id="field-password"]/label'],
        "密码输入框": ['xpath', '//*[@id="password"]'],
        "登录按钮": ['xpath', '//*[@id="submit"]'],
        "使用验证码登录": ['xpath', '//*[@id="login_form"]/div[2]/p'],
        "错误提示": ['id', 'login_error'],
        "版权所有": ['xpath', '/html/body/div[1]/div[3]/footer/div[1]/div/p'],
        "商标名称": ['xpath', '/html/body/div[1]/div[3]/footer/div[2]/div[1]/p'],

        "验证码账号": ["xpath", '//*[@id="login_code_form"]/fieldset/ol/li[1]/label'],
        "验证码账号输入框": ["xpath", '//*[@id="email-code"]'],
        "验证码": ["xpath", '//*[@id="login_code_form"]/fieldset/ol/li[2]/label'],
        "验证码输入框": ["xpath", '//*[@id="code-number-yz"]'],
        "获取验证码按钮": ["xpath", '//*[@id="login_code_form"]/fieldset/ol/li[2]/button'],
        "验证码登录按钮": ["xpath", '//*[@id="submit-code"]'],
        "验证码错误提示": ["xpath", '//*[@id="showError"]'],
        "使用账号密码登录": ["xpath", '//*[@id="login_code_form"]/div[2]/p'],

        "课程": ['id', 'course-index-tabs'],

    },

    "course_create":{
        #创建课程模块
        "创建课程按钮": ["css",
                   "#content > div.wrapper-mast.wrapper > header > nav > ul > li > a.button.new-button.new-course-button"],
        "创建课程标题": ["css", "#create-course-form > div.wrapper-form > h3"],
        "课程名称": ["css", "#field-course-name > label"],
        "课程名输入框": ["css", "#new-course-name"],
        "课程名备注": ["css", "#tip-new-course-name"],
        "组织机构": ["css", "#field-organization > label"],
        "组织机构输入框": ["css", "#new-course-org"],
        "组织机构备注": ["css", "#tip-new-course-org"],
        "课程编号": ["css", "#field-course-number > label"],
        "课程编号输入框": ["css", "#new-course-number"],
        "课程编号备注": ["css", "#tip-new-course-number"],
        "开课时间": ["css", "#field-course-run > label"],
        "开课时间输入框": ["css", "#new-course-run"],
        "开课时间备注": ["css", "#tip-new-course-run"],
        "课程分类": ["css", "#field-course-subject > label"],
        "新增分类": ["css", "#create-course-form > div.wrapper-form > fieldset > ol > div > div.add-coueseClassify-p"],
        "创建": ["css", "#create-course-form > div.actions > input.action.action-primary.new-course-save"],
        "取消": ["css",
               "#create-course-form > div.actions > input.action.action-secondary.action-cancel.new-course-cancel"],
        "课程编号组": ['css', 'div.course-metadata>span.course-num.metadata-item>span.value'],
        "重复提示": ["css", "#course_creation_error > p"]

    },

    "course_page": {
        # 课程内容页面模块
        # 缺笔记定位，"笔记": ["css", "#content > div.wrapper-content.wrapper > section > article > div.inner-wrapper > article > div.tab-list > ol > li:nth-child(6) > div.course-nav-item-header > h3"],
        "内容": ["css", "#content > div.wrapper-mast.wrapper > header > h1 > small"],
        "页面": ["css", "#content > div.wrapper-mast.wrapper > header > h1"],
        "在线查看": ["css", "#content > div.wrapper-mast.wrapper > header > nav > ul > li:nth-child(2) > a"],
        "注意": ["css", "#content > div.wrapper-content.wrapper > section > article > div.notice-incontext > p"],
        "主页": ["css",
               "#content > div.wrapper-content.wrapper > section > article > div.inner-wrapper > article > div.tab-list > ol > li:nth-child(1) > div.course-nav-item-header > h3"],
        "课程": ["css",
               "#content > div.wrapper-content.wrapper > section > article > div.inner-wrapper > article > div.tab-list > ol > li:nth-child(2) > div.course-nav-item-header > h3"],
        "讨论": ["css",
               "#content > div.wrapper-content.wrapper > section > article > div.inner-wrapper > article > div.tab-list > ol > li:nth-child(3) > div.course-nav-item-header > h3"],
        "Wiki": ["css",
                 "#content > div.wrapper-content.wrapper > section > article > div.inner-wrapper > article > div.tab-list > ol > li:nth-child(4) > div.course-nav-item-header > h3"],
        "进度": ["css",
               "#content > div.wrapper-content.wrapper > section > article > div.inner-wrapper > article > div.tab-list > ol > li:nth-child(5) > div.course-nav-item-header > h3"],

        "右问1": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(1) > h3"],
        "右答1": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(1) > p"],
        "右问2": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(2) > h3"],
        "右答2": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(2) > p"],
        "右问3": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(3) > h3"],
        "右答3": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(3) > p"],

        "进入课程": ["css",
                 "#content > div.wrapper-content.wrapper > section > article > div.courses.courses-tab.active > ul > li:nth-child(1) > a > h3"],
        "顶内容": ["css",
                "#view-top > header > div.wrapper.wrapper-l > nav > ol > li.nav-item.nav-course-courseware > h3 > span.label"],
        "顶页面": ["css",
                "#view-top > header > div.wrapper.wrapper-l > nav > ol > li.nav-item.nav-course-courseware > div > div > ul > li.nav-item.nav-course-courseware-pages > a"],

    },

    "course_outline": {
        # 课程内容大纲模块
        "顶内容": ["css",
                "#view-top > header > div.wrapper.wrapper-l > nav > ol > li.nav-item.nav-course-courseware > h3 > span.label"],
        "顶大纲": ["css",
               "#view-top > header > div.wrapper.wrapper-l > nav > ol > li.nav-item.nav-course-courseware > div > div > ul > li.nav-item.nav-course-courseware-outline"],
        "新增章固定": ["css", "#content > div.wrapper-mast.wrapper > header > nav > ul > li:nth-child(1) > a"],
        "新增章无内容时": ["css",
                    "#content > div.wrapper-content.wrapper > section > article > div.wrapper-dnd > article > div > p > a"],
        "新增章有内容时": ["css",
                    "#content > div.wrapper-content.wrapper > section > article > div.wrapper-dnd > article > div > div > a"],
        "课程大纲": ["css", "#content > div.wrapper-mast.wrapper > header > h1"],
        "折叠所有章节": ["css",
                   "#content > div.wrapper-mast.wrapper > header > nav > ul > li:nth-child(2) > a > span.collapse-all > span.label"],
        "在线查看": ["css", "#content > div.wrapper-mast.wrapper > header > nav > ul > li:nth-child(3) > a"],
        "课程开始日期": ["css", "#content > div.wrapper-content.wrapper > section > article > div.course-status > div > h2"],
        "开始时间设置": ["css", "#content > div.wrapper-content.wrapper > section > article > div.course-status > div > p"],
        "说明标题1": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(1) > h3"],
        "说明内容1.1": ["css",
                    "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(1) > p:nth-child(2)"],
        "说明内容1.2": ["css",
                    "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(1) > p:nth-child(3)"],
        "说明标题2": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(2) > h3"],
        "说明内容2": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(2) > p"],
        "了解更多2": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(2) > div > a"],
        "说明标题3": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(3) > h3"],
        "说明内容3": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(3) > p"],
        "了解更多3": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(3) > div > a"],
        "说明标题4": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(4) > h3"],
        "说明内容4.1": ["css",
                    "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(4) > p:nth-child(2)"],
        "说明内容4.2": ["css",
                    "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(4) > p:nth-child(3)"],
        "说明内容4.3": ["css",
                    "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(4) > p:nth-child(4)"],
        "了解更多4": ["css", "#content > div.wrapper-content.wrapper > section > aside > div:nth-child(4) > div > a"],
        # "新增节": ["css", ""],
        # "新增单元": ["css", ""],
        # "": ["css", ""],
    },


    "live_login": {  # 登录
        "登录框图片": ["css", "div.login-panel-header>img"],
        "账号文本": ["css","#root > div > div.main___2jCiI > form > div.ant-tabs.ant-tabs-top.tabs___R4MnG.ant-tabs-line.ant-tabs-no-animation > div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab-active.ant-tabs-tab"],
        "账号输入框": ["css", "#username"],
        "密码输入框": ["css", "#password"],
        "自动登录": ["css","#root > div > div.main___2jCiI > form > div.ant-row.ant-form-item.additional___2VbIO > div > div > span > label > span:nth-child(2)"],
        "忘记密码": ["css","#root > div > div.main___2jCiI > form > div.ant-row.ant-form-item.additional___2VbIO > div > div > span > a"],
        "登录": ["css","#root > div > div.main___2jCiI > form > div.ant-row.ant-form-item.additional___2VbIO > div > div > span > button"],
        "账户错误提示": ["css","#root > div > div.main___2jCiI > form > div.ant-tabs.ant-tabs-top.tabs___R4MnG.ant-tabs-line.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(1) > div > div > div"],
        "密码错误提示": ["css","#root > div > div.main___2jCiI > form > div.ant-tabs.ant-tabs-top.tabs___R4MnG.ant-tabs-line.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-row.ant-form-item.ant-form-item-with-help > div > div > div"],
        "错误提示": ["xpath", '//*[@id="root"]/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div/div/div'],

    },

    "live_list": {
        "title": ["css", "#root > div > div > div.ant-layout > div.header___1L3tU.ant-layout-header > div.companyname___1f2e8"],
        "直播列表": ["css", "#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div > div > div.ant-card-head > div > div.ant-card-head-title"],
        "创建直播": ["xpath", '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/a/button/span'],
        "页数": ["css", "#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div > div > div.ant-card-body > div > div.ant-list-pagination > ul > li.ant-pagination-options > div"],
        "创建直播按钮": ["css", 'button.ant-btn.ant-btn-primary'],
        "开始直播": ["css","#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div > div > div.ant-card-body > div > div.ant-spin-nested-loading > div > div:nth-child(1) > ul > li:nth-child(1) > a"],
        "更多操作": ["css","#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div > div > div.ant-card-body > div > div.ant-spin-nested-loading > div > div:nth-child(1) > ul > li:nth-child(2) > a"],
        "编辑直播": ["linktext", "编辑直播"],
        "观看直播": ["linktext", "观看直播"],
        "删除直播": ["linktext", "删除直播"],
        "确认": ["css", "div.ant-confirm-btns>button.ant-btn.ant-btn-danger"],
        "取消": ["css", "div.ant-confirm-btns>button.ant-btn"],
        "直播标题": ["css", "div.ant-spin-container>div.ant-list-item>div.ant-list-item-meta>div.ant-list-item-meta-content"],
        "删除提示框标题":["css", "div.ant-confirm-body-wrapper>div.ant-confirm-body>span.ant-confirm-title"],


    },
    "live_create": {
        "创建直播标题": ["css", "h1.title___3uDQf"],
        "直播标题": ["css", "div.ant-form-item-label.ant-col-sm-4"],
        "直播标题提示内容": ["id", "title"],
        "0/30": ["css", "span.titleSize___2A3MC"],
        "选择日期提示内容": ["css", "input.ant-calendar-picker-input.ant-input"],
        "选择时间": ["id", "live_datetime"],
        "选择时间提示内容": ["xpath", "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div[2]/div/span/div[2]/div/div/span/span/input"],
        "时区选择": ["css", "button.ant-btn.ant-dropdown-trigger"],
        "直播简介": ["xpath", "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[3]/div[1]/label/span"],
        "直播简介输入框": ["id", "intro"],
        "自动录制": ["xpath", "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[4]/div[1]/span"],
        "观看权限": ["xpath", "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div[1]/span"],
        "提示1": ["css", "div.authTips___3dMDc"],
        "提示2": ["css", "div.posterContianer___23RGU>div:first-child"],
        "提示3": ["css", "div.posterContianer___23RGU>div:nth-child(2)"],
        "建议尺寸": ["css", "div.posterExtends___1ZkSZ>span:first-child"],
        "支持": ["css", "div.posterContianer___23RGU>div>span:nth-child(3)"],
        "创建": ["css", "button.ant-btn.ant-btn-primary"],
        "取消": ["css", "div.basicOp___2oIOh>a>button.ant-btn"],
        "x按钮": ["css", "i.anticon.anticon-close-circle.titleClear___1npBV"],
        "日期x按钮": ["css","i.anticon.anticon-cross-circle.ant-calendar-picker-clear"],
        "时间x按钮": ["css","html body div div div.ant-time-picker-panel.ant-time-picker-panel-narrow.ant-time-picker-panel-column-2.ant-time-picker-panel-placement-bottomLeft div.ant-time-picker-panel-inner div.ant-time-picker-panel-input-wrap a.ant-time-picker-panel-clear-btn"],
        "选择的时间": ["css", "html body div div div.ant-calendar-picker-container.ant-calendar-picker-container-placement-bottomLeft div.ant-calendar div.ant-calendar-panel div.ant-calendar-date-panel div.ant-calendar-body table.ant-calendar-table tbody.ant-calendar-tbody tr td.ant-calendar-cell.ant-calendar-next-month-btn-day div.ant-calendar-date"],
        "时选择": ["css", "div.ant-time-picker-panel-combobox>div.ant-time-picker-panel-select>ul>li.ant-time-picker-panel-select-option-selected"],
        "分选择": ["css", "div.ant-time-picker-panel-combobox>div.ant-time-picker-panel-select>ul>li.ant-time-picker-panel-select-option-selected"],
        "时间": ["id", "live_datetime"],
        "凭密码进入": ["xpath", '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div[2]/div/div[1]/div[2]'],
        "密码_1": ["css", "div.authTips___3dMDc"],
        "密码_2": ["xpath", "/html/body/div/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div[2]/div/div[2]/div[2]"],
        "密码_3": ["css", "#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div.content___13wW7 > div > div > div > div:nth-child(1) > div.ant-col-xs-24.ant-col-lg-10 > div > div > div > div:nth-child(1)"],
        "密码_4": ["css", "div.posterTips___iNA2-"],
        "付费可见": ["xpath", '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div[2]/div/div[1]/div[3]'],
        "付_1": ["css", "div.authTips___3dMDc"],
        "指定用户可见": ["xpath", '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div/div[5]/div[2]/div/div[1]/div[4]'],
        "指_1": ["css", "div.authTips___3dMDc"],
        "金额输入": ["id", "charge"],
        "加金额": ['css', '#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div.content___13wW7 > div > div > div > div:nth-child(1) > div.ant-col-xs-24.ant-col-lg-14 > div > div:nth-child(5) > div.ant-col-xs-24.ant-col-sm-20 > div > div:nth-child(2) > div:nth-child(3) > div.ant-form-item-control-wrapper.ant-col-sm-20 > div > span > div > div.ant-input-number-handler-wrap > span.ant-input-number-handler.ant-input-number-handler-up'],
        "减金额": ['css', '#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div.content___13wW7 > div > div > div > div:nth-child(1) > div.ant-col-xs-24.ant-col-lg-14 > div > div:nth-child(5) > div.ant-col-xs-24.ant-col-sm-20 > div > div:nth-child(2) > div:nth-child(3) > div.ant-form-item-control-wrapper.ant-col-sm-20 > div > span > div > div.ant-input-number-handler-wrap > span.ant-input-number-handler.ant-input-number-handler-down'],
        "试听开关": ['css', '#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div.content___13wW7 > div > div > div > div:nth-child(1) > div.ant-col-xs-24.ant-col-lg-14 > div > div:nth-child(5) > div.ant-col-xs-24.ant-col-sm-20 > div > div:nth-child(2) > div:nth-child(4) > div.ant-form-item-control-wrapper.ant-col-sm-20 > div > span > span.ant-switch.ant-switch-checked'],
        "试听时间": ["id", "trial_time"],
        "增加试听时间": ["css", "html body div#root div.screen-md div.ant-layout.ant-layout-has-sider div.ant-layout div.ant-layout-content div div div.cardStyle___3RHP9 div div.ant-row div.ant-col-xs-24.ant-col-lg-14 div div.ant-row div.ant-col-xs-24.ant-col-sm-20 div div div.ant-row.ant-form-item.trialItem___FXuEX div.ant-form-item-control-wrapper.ant-col-sm-20 div.ant-form-item-control.has-success span.ant-form-item-children div.ant-input-number div.ant-input-number-handler-wrap span.ant-input-number-handler.ant-input-number-handler-up"],
        "减少试听时间": ["css", "#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div.content___13wW7 > div > div > div > div:nth-child(1) > div.ant-col-xs-24.ant-col-lg-14 > div > div:nth-child(5) > div.ant-col-xs-24.ant-col-sm-20 > div > div:nth-child(2) > div:nth-child(4) > div.ant-form-item-control-wrapper.ant-col-sm-20 > div > span > div > div.ant-input-number-handler-wrap > span.ant-input-number-handler.ant-input-number-handler-down"],
        "上传图片": ["css", "#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div.content___13wW7 > div > div > div > div:nth-child(1) > div.ant-col-xs-24.ant-col-lg-10 > div > div > div > div.basicPoster___1eolH"],
        "upload": ["id", "ossFile"],

    },
    'admin_login':{
        '中文': ['css', 'body > div.language > ul > li.language-active > a'],
        '登录按钮': ['id', 'btn_login'],
        '忘记密码': ['id', 'forget_password'],
        '验证码登录': ['css', '.pull-right.code-btn'],
        '账号输入框': ['id', 'login_user_email'],
        '密码输入框': ['id', 'login_password'],
        '错误提示': ['id', 'show_error']
    },
    'text_baidu':{
        "百度输入框":['id', 'kw'],
        "11111":['css', 'language-active > a:nth-child(1)']

    }
}
#Page_Text 存放对应模块的所有文本信息
Page_Text = {

    "cms_login": [
        "帮助",
        "登录",
        "登录到课程管理中心",
        "邮箱或手机号码",
        "例如：username@domain.com或者13800138000",
        "密码",
        "登录到课程管理中心",
        "使用验证码登录",
        "© 2018 英荔教育.",
        "EdX、Open edX、Studio和 edX、Open edX 图标是 edX 公司的（注册）商标。",

    ],

    "cms_login1": [
        "邮箱或手机号码",
        "例如：username@domain.com或者13800138000",
        "验证码",
        "获取验证码",
        "登录到课程管理中心",
        "使用账号密码登录",

    ],

    "course_create_string": [
        "创建新课程",
        "课程名称",
        "例如，计算机科学导论",
        "课程的公开显示名称。您可以在“高级设置”中对其进行修改。",
        "组织机构",
        "例如：XX大学或XX机构",
        "开设该课程的组织名称。注意：课程网址将包含该组织名称。您可以在“高级设置”中对其进行修改。",
        "课程编号",
        "例如： CS101",
        "这是组织内该课程的专有编号。注意：课程网址包含该编号，请勿输入空格和特殊字符。该编号不可修改。",
        "开课时间",
        "例如：2014_T1",
        "课程开课时间。注意：课程网址包含该时间，请勿输入空格和特殊字符。该时间不可修改。",
        "课程分类",
        "+新增分类",
        "创建",
        "取消",

    ],

    # 缺笔记文本，"笔记",
    "course_page_string": [
        "内容",
        "内容\n>\n页面",
        "在线查看",
        "注意：页面公开可见。如果用户访问链接即可看到页面，即使他们尚未注册或者登录课程。",
        "主页",
        "课程",
        "讨论",
        "Wiki",
        "进度",
        "什么是页面？",
        "页面在您课程页面的顶端水平展开。默认页面（主页、课程、讨论、课程百科和进度）的后面是教材页面和您创建的自定义页面。",
        "自定义页面",
        "您可以创建和编辑个性化页面，为学员提供额外的课程内容。例如，您可以创建评分政策、课程幻灯片和课程日历的自定义页面。",
        "在课程中，学员将会看到怎样的页面？",
        "学员将在课程上方看到默认页面以及自定义页面，通过点击不同的图标进行导航。\n请看例子",

    ],

    "course_outline_string": [
        "内容\n>\n课程大纲",
        "课程开始日期：",
        "添加新章节",
        "在线查看",
        "创建您课程的结构",
        "您可以直接在大纲中添加章、节和单元。",
        "创建章后，可在其中添加节和单元。然后在单元内添加课程组件。",
        "重新组织您的课程",
        "在大纲中将章，节和单元拖动至新的位置。",
        "了解更多",
        "设置课程开放日期和评分政策",
        "选择“设置”图标来为章、节设置开放日期。在设置节时，您还可以设置评分政策及截止日期。",
        "了解更多",
        "变更学员所见内容",
        "请点击章、节或单元中的“发布”图标来发布草稿内容。",
        "若要让章、节或单元对学员不可见，选择该层级的“设置”图标，然后选择“对学员隐藏”选项。隐藏后的章、节和单元成绩将不计入总成绩中。",
        "截止日期到期后，若要对学员隐藏节内容，请选择该节的“设置”图标，然后选择“截止日期过后隐藏课程内容”。该节的成绩将计入总成绩中。",
        "了解更多",
    ],


    "live_login": [
        "账户密码登录",
        "crews",
        "eliteu123",
        "自动登录",
        "忘记密码",
        "登 录",
        "注册账户"
    ],
    "live_list": [
        "英荔直播平台",
        "直播列表",
        "开始直播",
        "更多操作",
        "创建直播",
        "跳至页"
    ],
    "list_string": [
        "请确认是否删除直播",
        "取 消",
        "确 认",
        "http://elitelive.beta.e-ducation.cn/#/dashboard/create",

        ],
    "create_string": [
        "创建直播",
        "直播标题",
        "一句话说明主题",
        "0/30",
        "选择日期",
        "选择时间",
        "UTC+8北京时间",
        "直播简介",
        "自动录制",
        "观看权限",
        "知道直播地址即可加入，无需任何限制",
        "宣传海报",
        "直播未开始时，观众进入直播间看到的海报。",
        "建议尺寸： 1280x800px，图片小于2MB",
        "支持.jpeg/.gif/.png/.bmp",
        "创 建",
        "取 消",
        "这个是直播标题的测试现在输入18个字",
        "我现在输入了超过30个字啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦",
        "测试输入刚好30个字符9999999999999999999",
        "这个是测试标题",
        "2018-05-30",
        "04:04",
        "参与者需输入正确的密码，方可观看。",
        "本场直播参与密码已自动生成",
        "宣传海报",
        "直播未开始时，观众进入直播间看到的海报。",
        "参与者需要付费（通过支付宝或微信支付）才能进入直播",
        "指定哪些用户可以进入直播。您可以在直播创建后，在学员页面添加用户名单。",

       ],
    "time_select": [
        "2018-06-01",
        "00:00",
    ],
    "create_all": [
        "这是一个测试标题",
        "这是一个比较简短的简介",
        "http://elitelive.beta.e-ducation.cn/#/dashboard/create",
    ],
    'test_baidu':[
        "我是梦妍大佬！",
    ],
    'admin_login':[
        "中文",
        "登录",
        "忘记密码",
        "验证码登录"

    ],



    }