# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote

class A51JobSpider(scrapy.Spider):
    name = '51_job'
    allowed_domains = []
    start_urls = ['http://www.51job.com/']
    custom_settings={
        'LOG_LEVEL': 'INFO',
        'CONCURRENT_REQUESTS': 10,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 10,
        'CONCURRENT_REQUESTS_PER_IP': 10,
        'DOWNLOAD_DELAY': 0.3,
    }
    item_list=['Java', 'C++', 'PHP', '数据挖掘', '搜索算法', '精准推荐', 'C', 'C#', '全栈工程师', '.NET', 'Hadoop', 'Python', 'Delphi', 'VB', 'Perl', 'Ruby', 'Node.js', 'Go', 'ASP', 'Shell', '区块链', '后端开发其它', 'HTML5', 'Android', 'iOS', 'WP', '移动开发其它', 'web前端', 'Flash', 'html5', 'JavaScript', 'U3D', 'COCOS2D-X', '前端开发其它', '深度学习', '机器学习', '图像处理', '图像识别', '语音识别', '机器视觉', '算法工程师', '自然语言处理', '测试工程师', '自动化测试', '功能测试', '性能测试', '测试开发', '游戏测试', '白盒测试', '灰盒测试', '黑盒测试', '手机测试', '硬件测试', '测试经理', '测试其它', '运维工程师', '运维开发工程师', '网络工程师', '系统工程师', 'IT支持', 'IDC', 'CDN', 'F5', '系统管理员', '病毒分析', 'WEB安全', '网络安全', '系统安全', '运维经理', '运维其它', 'MySQL', 'SQLServer', 'Oracle', 'DB2', 'MongoDB', 'ETL', 'Hive', '数据仓库', 'DBA其它', '技术经理', '技术总监', '架构师', 'CTO', '运维总监', '技术合伙人', '项目总监', '测试总监', '安全专家', '高端技术职位其它', '项目经理', '项目助理', '硬件', '嵌入式', '自动化', '单片机', '电路设计', '驱动开发', '系统集成', 'FPGA开发', 'DSP开发', 'ARM开发', 'PCB工艺', '模具设计', '热传导', '材料工程师', '精益工程师', '射频工程师', '硬件开发其它', '实施工程师', '售前工程师', '售后工程师', 'BI工程师', '企业软件其它', '产品经理', '网页产品经理', '移动产品经理', '产品助理', '数据产品经理', '电商产品经理', '游戏策划', '产品实习生', '网页产品设计师', '无线产品设计师', '产品部经理', '产品总监', '游戏制作人', '视觉设计师', '网页设计师', 'Flash设计师', 'APP设计师', 'UI设计师', '平面设计师', '美术设计师（2D/3D）', '广告设计师', '多媒体设计师', '原画师', '游戏特效', '游戏界面设计师', '游戏场景', '游戏角色', '游戏动作', '交互设计师', '无线交互设计师', '网页交互设计师', '硬件交互设计师', '数据分析师', '用户研究员', '游戏数值策划', '设计经理/主管', '设计总监', '视觉设计经理/主管', '视觉设计总监', '交互设计经理/主管', '交互设计总监', '用户研究经理/主管', '用户研究总监', '用户运营', '产品运营', '数据运营', '内容运营', '活动运营', '商家运营', '品类运营', '游戏运营', '网络推广', '运营专员', '网店运营', '新媒体运营', '海外运营', '运营经理', '副主编', '内容编辑', '文案策划', '记者', '售前咨询', '售后客服', '淘宝客服', '客服经理', '主编', '运营总监', 'COO', '客服总监', '市场营销', '市场策划', '市场顾问', '商务渠道', '商业数据分析', '活动策划', '网络营销', '海外市场', '商务专员', '政府关系', '品牌公关', '广告协调', '媒介投放', '媒介合作', '媒介顾问', '广告创意', '广告制作', '广告文案', '广告投放', '广告定价', '广告专员', '品牌合作', '品牌策划', '品牌专员', '美术指导', '市场推广', '渠道推广', 'SEO', 'SEM', '策划经理', '媒介经理', '市场总监', '公关总监', '媒介总监', '创意总监', '销售专员', '销售顾问', '销售经理', '客户代表', '大客户代表', '客户经理', '商务拓展', '渠道销售 ', '代理商销售', '电话销售', '广告销售', '信用卡销售', '保险销售', '销售工程师', '商务渠道', '其他销售', '销售总监', '商务总监', '区域总监', '城市经理', '团队经理', '销售VP', '商务主管', '其他销售管理职位', '人力资源', '招聘', 'HRBP', '人事/HR', '培训经理', '薪资福利经理', '绩效考核经理', '员工关系', '助理', '前台', '行政', '总助', '文秘', '会计', '出纳', '财务', '结算', '税务', '审计', '风控', '法务', '律师', '专利', '行政总监/经理', '财务总监/经理', 'HRD/HRM', 'CFO', 'CEO', 'H5游戏开发', '小游戏开发', '游戏后端开发', 'C++游戏开发', 'FLASH', 'COCOS2D-X', 'U3D', '游戏测试', '游戏制作人', '游戏产品经理', '游戏项目经理', '游戏策划', '剧情设计', '游戏文案', '游戏动画', '游戏原画', '游戏界面', '游戏场景', '游戏角色', '游戏动作', '游戏动效', '游戏美工', '游戏运营', '游戏编辑', '游戏推广', '手游推广', '页游推广', '游戏主播', '游戏陪练', '游戏体验', '电竞主持', '电竞讲师']

    def __init__(self,**kwargs):
        scrapy.Spider.__init__(self)
        # 可以传递 地址参数
        self.jobarea=kwargs.get('jobarea') if kwargs.get('jobarea') else '000000'

    def parse(self, response):
        for url in response.css('div.el p.t1 span a::attr(href)').extract():
            self.logger.info(f"开始爬取:{url}")
            yield scrapy.Request(url,callback=self.parse_data)

    #     TODO 下一页 可以加上

    def parse_data(self,response):
        item={}
        item['url']=response.url
        try:
            item['title']=response.css('div.cn>h1[title]::text').extract_first().split('\r\n\t')
        except:
            item['title']=""
        try:
            item['remake']=[x for x in response.css('div.cn>p.msg.ltype::attr(title)').extract_first().split('\xa0') if x and x != '|']
        except:
            item['remake']=[]
        item['welfare']=response.css('span.sp4::text').extract()
        item['text']=response.css('div.bmsg.job_msg.inbox p::text').extract()
        item['addr']="".join(response.css('div.tBorderTop_box div.bmsg.inbox p.fp::text').extract()).strip('\r\n\t')
        item['name']=response.css('div.com_msg a.com_name p::text').extract_first()
        self.logger.info(f'爬取成功:{item["url"]}')
        yield item

    def start_requests(self):
        for keyword in self.item_list:
            ind = '00'
            fun = '0000'
            jobarea = self.jobarea
            specialarea = '00'
            keywordtype = '2'
            workyear = '99'
            cottype = '99'
            degreefrom = '99'
            jobterm = '99'
            companysize = '99'
            providesalary = '99'
            postchannel = '0000'
            url = f"https://search.51job.com/list/{quote(jobarea)},000000,{quote(quote(fun))},{quote(quote(ind))},9,99,{quote(quote(keyword))},{quote(quote(keywordtype))},1.html?lang=c&stype=&postchannel={postchannel}&workyear={workyear}&cotype={cottype}&degreefrom={degreefrom}&jobterm={jobterm}&companysize={companysize}&providesalary={providesalary}&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea={specialarea}&from=&welfare='"
            yield scrapy.Request(url)