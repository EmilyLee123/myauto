#config_element对应模块的所有的元素定位
config_element = {
        "live_login": {#登录
                "登录框图片": ["css", "div.login-panel-header>img"],
                "账号文本": ["css", "#root > div > div.main___2jCiI > form > div.ant-tabs.ant-tabs-top.tabs___R4MnG.ant-tabs-line.ant-tabs-no-animation > div.ant-tabs-bar > div > div > div > div > div.ant-tabs-tab-active.ant-tabs-tab"],
                "账号输入框": ["css", "#username"],
                "密码输入框": ["css", "#password"],
                "自动登录": ["css", "#root > div > div.main___2jCiI > form > div.ant-row.ant-form-item.additional___2VbIO > div > div > span > label > span:nth-child(2)"],
                "忘记密码": ["css", "#root > div > div.main___2jCiI > form > div.ant-row.ant-form-item.additional___2VbIO > div > div > span > a"],
                "登录": ["css", "#root > div > div.main___2jCiI > form > div.ant-row.ant-form-item.additional___2VbIO > div > div > span > button"],
                "账户错误提示": ["css", "#root > div > div.main___2jCiI > form > div.ant-tabs.ant-tabs-top.tabs___R4MnG.ant-tabs-line.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(1) > div > div > div"],
                "密码错误提示": ["css", "#root > div > div.main___2jCiI > form > div.ant-tabs.ant-tabs-top.tabs___R4MnG.ant-tabs-line.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-row.ant-form-item.ant-form-item-with-help > div > div > div"],
                "错误提示": ["xpath", '//*[@id="root"]/div/div[2]/form/div[1]/div[2]/div[1]/div[2]/div/div/div'],
               

        },
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
            "错误提示": ['xpath', '//*[@id="login_error"]'],
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

        },
        "live_list": {
            "title": ["css", "#root > div > div > div.ant-layout > div.header___1L3tU.ant-layout-header > div.companyname___1f2e8"],
            "直播列表": ["css", "#root > div > div > div.ant-layout > div.ant-layout-content > div:nth-child(1) > div > div > div > div.ant-card-head > div > div.ant-card-head-title"],
            "开始直播": ["xpath", '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/ul/li[1]/a'],
            "更多操作": ["xpath", '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/ul/li[2]/a'],
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


    }