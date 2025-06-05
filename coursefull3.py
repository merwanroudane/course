
import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt # Removed as plotly will be used
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
from PIL import Image
import io

# Page configuration
st.set_page_config(
	page_title="دورة القياس الاقتصادي المتقدمة 2025",
	page_icon="📊",
	layout="wide",
	initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        direction: rtl;
        text-align: right;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        direction: rtl;
        text-align: right;
        white-space: pre-wrap;
    }
    h1, h2, h3, h4, h5, h6 {
        direction: rtl;
        text-align: right;
    }
    .stMarkdown {
        direction: rtl;
        text-align: right;
    }
    .highlight {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .course-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        border-left: 5px solid #4e89ae;
    }
    .price-tag {
        background-color: #4e89ae;
        color: white;
        font-weight: bold;
        padding: 5px 10px;
        border-radius: 5px;
        display: inline-block;
        margin-top: 10px;
    }
    .feature-box {
        background-color: #eef2f5;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid #2c3e50;
    }
    .btn-register {
        background-color: #2c3e50;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 10px 0;
        cursor: pointer;
        border-radius: 5px;
        border: none;
    }
    .btn-register:hover {
        background-color: #4e89ae;
    }
    .footer {
        margin-top: 30px;
        padding: 20px;
        text-align: center;
        background-color: #f0f2f6;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
	st.title("القائمة")
	# Initialize session state for navigation if not already done
	if "nav" not in st.session_state:
		st.session_state.nav = "الصفحة الرئيسية"

	nav_options = ["الصفحة الرئيسية", "محتوى الدورة", "النماذج الإحصائية", "تقنيات Wavelet", "البرمجيات", "التسجيل",
				   "الأسئلة الشائعة"]
	# Get the index of the current navigation state for st.radio
	try:
		current_nav_index = nav_options.index(st.session_state.nav)
	except ValueError:
		current_nav_index = 0  # Default to home if current state is invalid

	nav = st.radio(
		"انتقل إلى:",
		nav_options,
		index=current_nav_index,
		key="sidebar_nav"  # Add a key to make it controllable
	)
	# Update session state if radio button changes
	if nav != st.session_state.nav:
		st.session_state.nav = nav
		st.experimental_rerun()

	st.divider()
	st.write("معلومات الاتصال:")
	st.write("البريد الإلكتروني: course2025a@gmail.com")
	st.write("المدرب: د. مروان رودان")

	with st.expander("معلومات الدورة"):
		st.write("الرسوم للطلاب الدوليين: 80 دولار أمريكي")
		st.write("الرسوم للطلاب الجزائريين: 7,000 دينار جزائري")
		st.write("ستبدأ الدورة عند الوصول إلى الحد الأدنى من المشاركين")

# Main content
if st.session_state.nav == "الصفحة الرئيسية":
	col1, col2 = st.columns([3, 1])

	with col1:
		st.title("دورة القياس الاقتصادي المتقدمة 2025")
		st.subheader("دورة شاملة في النماذج الإحصائية التقليدية والحديثة")
		st.markdown("### 150 نموذج إحصائي متقدم")
		st.markdown("*تدريب عملي على القياس الاقتصادي التطبيقي*")

		st.markdown("---")
		st.markdown("### نظرة عامة على الدورة")
		st.markdown("""
        توفر هذه الدورة الشاملة في القياس الاقتصادي تدريباً مكثفاً على منهجيات القياس الاقتصادي التقليدية والحديثة، 
        وتغطي 150 نموذجاً مختلفاً مطبقة على مختلف أنواع البيانات والمجالات الاقتصادية. 
        تركز الدورة على التطبيق العملي باستخدام منصات برمجية متعددة.
        """)

		st.markdown("### مميزات الدورة")
		st.markdown("""
        <div class="feature-box">
            <h4>✅ شهادة مرموقة عند إكمال الدورة</h4>
            شهادة معتمدة تضيف قيمة إلى سيرتك الذاتية وتعزز فرصك المهنية
        </div>

        <div class="feature-box">
            <h4>✅ دورة مجانية للمبتدئين</h4>
            قبل بداية الدورة الرئيسية، يحصل المبتدئون على دورة تمهيدية مجانية في أساسيات القياس الاقتصادي
        </div>

        <div class="feature-box">
            <h4>✅ محاضرات في أساسيات البرمجيات</h4>
            في بداية الدورة، ستتلقى محاضرات إضافية حول أساسيات البرمجيات المستخدمة (R, Python, MATLAB, Stata, EViews)
        </div>

        <div class="feature-box">
            <h4>✅ كتاب تفاعلي PDF</h4>
            ستحصل على كتاب تفاعلي بتنسيق PDF يحتوي على كامل محتوى الدورة للرجوع إليه في أي وقت
        </div>

        <div class="feature-box">
            <h4>✅ تخصيص المحتوى</h4>
            عند التسجيل، يمكنك إضافة النماذج التي ترغب في التركيز عليها وتعلمها
        </div>

        <div class="feature-box">
            <h4>✅ تقنيات Wavelet المتقدمة</h4>
            تتضمن الدورة تقنيات تحليل المويجات (Wavelet) ودمجها مع مختلف التحليلات الإحصائية
        </div>
        """, unsafe_allow_html=True)

	with col2:
		# Placeholder for course logo/image
		st.image("https://via.placeholder.com/300x200?text=Econometrics+Course", use_column_width=True)

		st.markdown("### الجدول الزمني")
		st.markdown("ثلاث جلسات أسبوعياً")
		st.markdown("تستمر حتى الوصول للعدد المطلوب من المشاركين")

		st.markdown("### رسوم الدورة")
		st.markdown("الطلاب الدوليين: $80 USD")
		st.markdown("الطلاب الجزائريين: 7,000 DA")

		st.markdown("### سجل الآن")
		if st.button("التسجيل في الدورة", key="register_home"):
			st.session_state.nav = "التسجيل"  # Use st.session_state for navigation
			st.experimental_rerun()

	st.markdown("---")
	st.markdown("### الفئة المستهدفة")
	col1, col2 = st.columns(2)

	with col1:
		st.markdown("""
        • طلاب الدراسات العليا في الاقتصاد والمالية والمجالات ذات الصلة
        • الباحثون والأكاديميون
        • محللي السياسات والاقتصاديون الحكوميون
        """)

	with col2:
		st.markdown("""
        • المحللون الماليون ومديرو المخاطر
        • علماء البيانات العاملون مع البيانات الاقتصادية
        • المهنيون الذين يسعون لاكتساب مهارات متقدمة في القياس الاقتصادي
        """)

elif st.session_state.nav == "محتوى الدورة":
	st.title("محتوى دورة القياس الاقتصادي المتقدمة")

	tab1, tab2, tab3, tab4, tab5 = st.tabs(
		["أنواع البيانات", "مجالات التطبيق", "مخرجات التعلم", "تنسيق الدورة", "نظرة عامة"])

	with tab1:
		st.markdown("## أنواع البيانات المغطاة في الدورة")

		col1, col2 = st.columns(2)

		with col1:
			st.markdown("### تحليل البيانات المقطعية")
			st.markdown("""
            • نماذج الانحدار الخطية وغير الخطية
            • نماذج المتغيرات التابعة المحدودة
            • نماذج اختيار العينة
            • انحدار الكمية
            """)

			st.markdown("### تحليل السلاسل الزمنية")
			st.markdown("""
            • نماذج ARIMA والنماذج الموسمية
            • متجه الانحدار الذاتي (VAR)
            • نماذج التكامل المشترك وتصحيح الخطأ
            • نماذج GARCH وتقلب الأسعار
            • نماذج الحالة المكانية
            """)

			st.markdown("### اقتصاد قياسي للبيانات الطولية")
			st.markdown("""
            • نماذج التأثيرات الثابتة والعشوائية
            • نماذج البيانات الطولية الديناميكية
            • اختبارات جذر الوحدة والتكامل المشترك للبيانات الطولية
            • نماذج البيانات الطولية المكانية
            """)

		with col2:
			st.markdown("### القياس الاقتصادي المكاني")
			st.markdown("""
            • نماذج الانحدار الذاتي المكاني
            • نماذج الخطأ المكاني
            • الانحدار المرجح جغرافياً
            • نماذج البيانات الطولية المكانية
            """)

			st.markdown("### تحليل البيانات النصية")
			st.markdown("""
            • استخراج النصوص للتحليل الاقتصادي
            • تحليل المشاعر في التمويل
            • نمذجة الموضوعات
            • تطبيقات معالجة اللغة الطبيعية
            """)

			st.markdown("### تقنيات Wavelet (المويجات)")
			st.markdown("""
            • تحليل المويجات المتقطعة (DWT)
            • تحليل المويجات المستمرة (CWT)
            • تحويلات المويجات المتعددة
            • دمج تقنيات المويجات مع نماذج السلاسل الزمنية
            • تطبيقات المويجات في التنبؤ المالي والاقتصادي
            """)

	with tab2:
		st.markdown("## مجالات التطبيق")

		col1, col2, col3 = st.columns(3)

		with col1:
			st.markdown("### القياس الاقتصادي المالي")
			st.markdown("""
            • نماذج تسعير الأصول
            • إدارة المخاطر
            • تحسين المحفظة
            • تحليل البيانات عالية التردد
            • تحليل العملات المشفرة
            """)

			st.markdown("### الاقتصاد الكلي")
			st.markdown("""
            • تحليل دورة الأعمال
            • نماذج السياسة النقدية
            • نماذج النمو
            • التنبؤ بالتضخم
            • نماذج DSGE
            """)

		with col2:
			st.markdown("### الاقتصاد الجزئي")
			st.markdown("""
            • نماذج اختيار المستهلك
            • تقدير دالة الإنتاج
            • تحليل هيكل السوق
            • الاقتصاد السلوكي
            • تحليل البيانات التجريبية
            """)

			st.markdown("### التجارة الدولية")
			st.markdown("""
            • نماذج الجاذبية
            • تحليل تدفق التجارة
            • نماذج أسعار الصرف
            • تحليل القدرة التنافسية
            • اتفاقيات التجارة الإقليمية
            """)

		with col3:
			st.markdown("### اقتصاديات التنمية")
			st.markdown("""
            • تحليل الفقر
            • تقييم الأثر
            • الاقتصاد الزراعي
            • اقتصاديات الصحة
            • اقتصاديات التعليم
            """)

			st.markdown("### اقتصاديات البيئة")
			st.markdown("""
            • نماذج تغير المناخ
            • اقتصاديات الموارد
            • تحليل التلوث
            • اقتصاديات الطاقة
            • مقاييس الاستدامة
            """)

	with tab3:
		st.markdown("## مخرجات التعلم")
		st.markdown("عند الانتهاء من الدورة، سيكون المشاركون قادرين على:")

		col1, col2 = st.columns(2)

		with col1:
			st.markdown("""
            1. تطبيق النماذج الإحصائية المناسبة لمختلف أنواع البيانات
            2. تنفيذ تقنيات القياس الاقتصادي المتقدمة باستخدام منصات برمجية متعددة
            3. إجراء تحليل تجريبي دقيق في مختلف المجالات الاقتصادية
            """)

		with col2:
			st.markdown("""
            4. تفسير وعرض نتائج القياس الاقتصادي بشكل احترافي
            5. التعامل مع مجموعات البيانات المعقدة بما في ذلك البيانات المكانية والنصية
            6. تطوير واختبار الفرضيات الاقتصادية باستخدام أساليب القياس الاقتصادي الحديثة
            """)

	with tab4:
		st.markdown("## تنسيق الدورة")

		col1, col2 = st.columns(2)

		with col1:
			st.markdown("### الجدول")
			st.markdown("• ثلاث جلسات أسبوعياً")
			st.markdown("• تستمر حتى الوصول للعدد المطلوب من المشاركين")

			st.markdown("### التنسيق")
			st.markdown("• تدريب عملي تطبيقي مع مجموعات بيانات من العالم الحقيقي")

		with col2:
			st.markdown("### المواد")
			st.markdown("• توفير جميع أكواد البرمجيات ومجموعات البيانات وملاحظات المحاضرات")
			st.markdown("• كتاب تفاعلي بتنسيق PDF")

			st.markdown("### الميزات الإضافية")
			st.markdown("• دورة مجانية للمبتدئين قبل بداية الدورة الرئيسية")
			st.markdown("• محاضرات إضافية عن أساسيات البرمجيات")
			st.markdown("• إمكانية تخصيص المحتوى حسب احتياجات المشاركين")

	with tab5:
		st.markdown("## نظرة عامة على الدورة")
		st.markdown("""
        تقدم هذه الدورة الشاملة في القياس الاقتصادي تدريباً مكثفاً في منهجيات القياس الاقتصادي التقليدية والحديثة، 
        حيث تغطي 150 نموذجاً إحصائياً مختلفاً مطبقة على مختلف أنواع البيانات والمجالات الاقتصادية.

        الدورة تجمع بين النظرية والتطبيق العملي، مع التركيز على استخدام البرمجيات الإحصائية المختلفة
        لتحليل البيانات الاقتصادية وتفسير النتائج. كما تتضمن الدورة تقنيات wavelet المتقدمة ودمجها
        مع مختلف التحليلات الإحصائية.

        تم تصميم الدورة لتلبية احتياجات مجموعة واسعة من المشاركين، من طلاب الدراسات العليا إلى
        المهنيين العاملين في مجالات الاقتصاد والمالية وعلوم البيانات.
        """)

		st.markdown("### مزايا فريدة")
		st.markdown("""
        - تغطية شاملة لـ 150 نموذجاً إحصائياً متقدماً
        - تطبيقات عملية باستخدام بيانات حقيقية
        - التدريب على خمس منصات برمجية مختلفة
        - دمج تقنيات wavelet المتقدمة مع التحليلات التقليدية
        - كتاب تفاعلي يحتوي على كامل المحتوى
        - شهادة معتمدة عند إكمال الدورة
        - إمكانية تخصيص المحتوى حسب احتياجات المشاركين
        """)

elif st.session_state.nav == "النماذج الإحصائية":
	st.title("النماذج الإحصائية المغطاة في الدورة")

	model_types = [
		"النماذج الأساسية والمقطعية",
		"نماذج السلاسل الزمنية (أحادية ومتعددة المتغيرات)",
		"نماذج البيانات الطولية",
		"نماذج القياس الاقتصادي المكاني",
		"نماذج الاستدلال السببي وتأثيرات المعالجة",
		"هجينة التعلم الآلي والقياس الاقتصادي",
		"تحليل البيانات النصية ومعالجة اللغة الطبيعية",
		"القياس الاقتصادي البايزي",
		"النماذج المتقدمة الهجينة الأخرى",
		"تقنيات Wavelet وتطبيقاتها"
	]

	# Create a dropdown to select model type
	selected_model_type = st.selectbox("اختر نوع النماذج", model_types)

	# Define model details for each type
	model_details = {
		"النماذج الأساسية والمقطعية": [
			"نماذج المربعات الصغرى العادية (OLS) وامتداداتها (WLS، Robust SE)",
			"النماذج الخطية المعممة (GLM)",
			"انحدار الكمية",
			"نماذج المتغيرات التابعة المحدودة (Logit، Probit، Tobit)",
			"نماذج اختيار العينة (مثل Heckman)",
			"نماذج بيانات العد (Poisson، ذي الحدين السالب، Zero-Inflated، Hurdle)",
			"الانحدار غير المعلمي (Kernel، Local Polynomial، Splines)",
			"النماذج شبه المعلمية (Partially Linear، Single Index، Varying Coefficient)"
		],
		"نماذج السلاسل الزمنية (أحادية ومتعددة المتغيرات)": [
			"امتدادات عائلة ARIMA: ARIMA، SARIMA، ARFIMA",
			"عائلة متجه الانحدار الذاتي (VAR): VAR، SVAR، VECM، BVAR، TVP-VAR، FAVAR، MS-VAR، GVAR، Sparse VAR، TVAR، Quantile VAR",
			"عائلة الانحدار الذاتي ذو الفجوات الموزعة (ARDL): ARDL، NARDL، CS-ARDL، TVP-ARDL",
			"نماذج التقلب (عائلة GARCH والتقلب العشوائي): ARCH، GARCH، EGARCH، GJR-GARCH، TGARCH، APARCH، FIGARCH، HYGARCH، Multivariate GARCH، Component GARCH، Spline GARCH، MS-GARCH، GARCH-MIDAS، Realized GARCH، نماذج التقلب العشوائي",
			"نماذج الحالة المكانية والعوامل الديناميكية: تمثيلات حالة المكان بمرشح كالمان، نماذج المكونات غير المرئية، نماذج حالة المكان المتغيرة زمنياً، نماذج العوامل الديناميكية",
			"نماذج السلاسل الزمنية غير الخطية: TAR، SETAR، STAR (LSTAR، ESTAR)، MS-AR",
			"نماذج السلاسل الزمنية المتخصصة الأخرى: MIDAS، CAViaR، ACD للبيانات عالية التردد"
		],
		"نماذج البيانات الطولية": [
			"البيانات الطولية الثابتة: التأثيرات الثابتة، التأثيرات العشوائية، OLS المجمعة",
			"نماذج البيانات الطولية الديناميكية (Arellano-Bond، Blundell-Bond GMM)",
			"اختبارات جذر الوحدة والتكامل المشترك للبيانات الطولية",
			"Panel VAR، Panel VECM",
			"Panel ARDL (مقدرات PMG، MG، DFE)",
			"نماذج العتبة للبيانات الطولية، انحدار الانتقال السلس للبيانات الطولية (PSTR)",
			"نماذج مع تأثيرات ثابتة تفاعلية (مثل Bai)",
			"التأثيرات المرتبطة الشائعة (CCE - Pesaran)، CCE الديناميكية",
			"نماذج البيانات الطولية المعززة بالعوامل",
			"انحدار الكمية للبيانات الطولية",
			"نماذج Probit/Logit الديناميكية للبيانات الطولية",
			"نماذج البيانات الطولية غير المتجانسة (Mean Group، Pooled Mean Group)",
			"البيانات الطولية مع الاعتماد المقطعي",
			"نماذج البيانات الطولية ذات المعاملات العشوائية"
		],
		"نماذج القياس الاقتصادي المكاني": [
			"نموذج الانحدار الذاتي المكاني (SAR)، نموذج الخطأ المكاني (SEM)",
			"نموذج دوربن المكاني (SDM)، نموذج الانحدار الذاتي المكاني المركب (SAC/SARAR)",
			"الانحدار المرجح جغرافياً (GWR)",
			"نماذج البيانات الطولية المكانية (SAR Panel، SEM Panel، SDM Panel، إلخ)",
			"نماذج البيانات الطولية المكانية الديناميكية",
			"نماذج الترشيح المكاني، مواصفات المصفوفة الأسية المكانية (MESS)"
		],
		"نماذج الاستدلال السببي وتأثيرات المعالجة": [
			"تصميم الانحدار المتقطع (RDD: حاد، غامض، امتدادات)",
			"الفرق في الفروق (DiD: أساسي، التبني المتدرج - مثل Callaway Sant'Anna، Goodman-Bacon، المعالجة المستمرة)",
			"طرق التحكم التركيبي (SCM، SC المعمم، SCM المعزز)",
			"المتغيرات الأداتية (IV: 2SLS، LIML، LATE، MTE)",
			"نهج دالة التحكم",
			"طرق المطابقة (مطابقة درجة الميل، الجار الأقرب، إلخ)",
			"الترجيح بالاحتمال المعكوس (IPW)",
			"المقدرات المتينة المزدوجة",
			"نماذج تحليل الوساطة"
		],
		"هجينة التعلم الآلي والقياس الاقتصادي": [
			"الانحدار المنتظم: LASSO، Ridge، Elastic Net",
			"الطرق القائمة على الأشجار: Random Forests، Causal Forests، Gradient Boosting (GBM، XGBoost، LightGBM)، Bayesian Additive Regression Trees (BART)",
			"الشبكات العصبية للقياس الاقتصادي: الشبكات العصبية التغذية الأمامية، الشبكات العصبية المتكررة (RNN، LSTM، GRU) للسلاسل الزمنية، الشبكات العصبية التلافيفية (CNN) لهياكل البيانات المحددة",
			"تقنيات التعلم الآلي الأخرى: Support Vector Regression (SVR)، Principal Component Regression (PCR)، Partial Least Squares (PLSR)، K-Nearest Neighbors (KNN) Regression",
			"هجينة الذكاء الاصطناعي والقياس الاقتصادي للاستدلال السببي والتنبؤ: Double/Debiased Machine Learning (DML)، Targeted Maximum Likelihood Estimation (TMLE)",
			"هجينة الذكاء الاصطناعي والقياس الاقتصادي للتنبؤ: التنبؤ الهجين للسلاسل الزمنية (مثل ARIMA-NN، Prophet)",
			"تقنيات متوسط النموذج التي تدمج التعلم الآلي (مثل Bayesian Model Averaging)"
		],
		"تحليل البيانات النصية ومعالجة اللغة الطبيعية": [
			"استخراج النصوص لإنشاء المتغيرات (Bag-of-Words، TF-IDF، N-grams)",
			"نماذج تحليل المشاعر (القائمة على القاموس، القائمة على التعلم الآلي)",
			"نمذجة الموضوعات (Latent Dirichlet Allocation - LDA، Structural Topic Models - STM)",
			"تضمينات الكلمات (Word2Vec، GloVe، BERT) لاستخراج الميزات الاقتصادية",
			"معالجة اللغة الطبيعية لتحليل السياسات (مثل تحليل خطابات البنوك المركزية، بيانات الأخبار)"
		],
		"القياس الاقتصادي البايزي": [
			"متجه الانحدار الذاتي البايزي (BVAR) - (مدرج أيضاً ضمن VAR)",
			"نماذج البيانات الطولية البايزية",
			"نماذج التقلب العشوائي البايزية",
			"التقدير البايزي لنماذج DSGE",
			"انحدار الكمية البايزي",
			"النماذج البايزية غير المعلمية (مثل نماذج خليط عملية ديريكليه)",
			"متوسط النموذج البايزي (BMA)"
		],
		"النماذج المتقدمة الهجينة الأخرى": [
			"نماذج التوازن العام الديناميكي العشوائي (DSGE): RBC، New Keynesian، Estimated DSGE، DSGE-VAR، Heterogeneous Agent NK - HANK",
			"نماذج قائمة على الوكلاء (ABM) - تقنيات المعايرة والتقدير",
			"النماذج القائمة على Copula (لنمذجة الاعتماد، مثل Copula-GARCH)",
			"تحليل البيانات الوظيفية (FDA) في القياس الاقتصادي",
			"نماذج اقتصاد قياسي للشبكات",
			"النهج النظري المعلوماتي (مثل Generalized Entropy)"
		],
		"تقنيات Wavelet وتطبيقاتها": [
			"أساسيات تحليل المويجات (Wavelet Analysis): تحويل المويجات المتقطعة (DWT)، تحويل المويجات المستمرة (CWT)",
			"تحليل تماسك المويجات (Wavelet Coherence Analysis) لدراسة العلاقات بين السلاسل الزمنية",
			"دمج تقنيات Wavelet مع نماذج ARIMA و VAR",
			"نماذج GARCH-Wavelet الهجينة للتنبؤ بتقلبات الأسواق المالية",
			"تحليل متعدد المقاييس (Multiscale Analysis) باستخدام تقنيات المويجات",
			"تحليل المويجات للكشف عن الدورات الاقتصادية والأنماط طويلة المدى",
			"استخدام تقنيات Wavelet في تحليل البيانات المالية عالية التردد",
			"تطبيقات Wavelet في اقتصاديات الطاقة وتحليل أسعار السلع",
			"طرق تقليل الضوضاء (Denoising) باستخدام المويجات للبيانات الاقتصادية",
			"نمذجة العلاقات غير الخطية باستخدام تحليل المويجات"
		]
	}

	# Display the selected models
	st.subheader(f"نماذج {selected_model_type}")

	for i, model in enumerate(model_details[selected_model_type]):
		with st.expander(f"{i + 1}. {model.split(':')[0]}" if ":" in model else f"{i + 1}. {model}"):
			if ":" in model:
				main_model, details = model.split(":", 1)
				st.markdown(f"**{main_model}**")
				st.markdown(details)
			else:
				st.markdown("سيتم تغطية هذا النموذج بالتفصيل في الدورة، مع التطبيق العملي والأمثلة.")

	st.markdown("---")
	st.info(
		"هذه قائمة توضيحية للنماذج التي سيتم تغطيتها في الدورة. ستتلقى تدريباً عملياً مفصلاً على كل نموذج مع أمثلة تطبيقية.")

	if st.button("سجل الآن للحصول على تدريب شامل على هذه النماذج", key="register_models"):
		st.session_state.nav = "التسجيل"  # Use st.session_state
		st.experimental_rerun()

elif st.session_state.nav == "تقنيات Wavelet":
	st.title("تقنيات Wavelet (المويجات) وتطبيقاتها في القياس الاقتصادي")

	st.markdown("""
    تعد تقنيات تحليل المويجات (Wavelet Analysis) من الأدوات المتقدمة في تحليل البيانات الاقتصادية والمالية، 
    حيث توفر رؤى فريدة للعلاقات متعددة المستويات والتغيرات الزمنية في الظواهر الاقتصادية. 
    في هذه الدورة، نقدم تدريباً شاملاً على تقنيات Wavelet ودمجها مع مختلف نماذج القياس الاقتصادي.
    """)

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("### الأساسيات النظرية")
		st.markdown("""
        - مقدمة في نظرية المويجات (Wavelet Theory)
        - تحويل المويجات المتقطعة (DWT) والمستمرة (CWT)
        - دوال المويجات المختلفة (Haar, Daubechies, Morlet, Mexican Hat)
        - تحليل تماسك المويجات (Wavelet Coherence)
        - التحليل متعدد المستويات (Multiresolution Analysis)
        """)

		st.markdown("### دمج Wavelet مع نماذج السلاسل الزمنية")
		st.markdown("""
        - نماذج ARIMA-Wavelet الهجينة
        - دمج تقنيات Wavelet مع نماذج VAR و VECM
        - نماذج GARCH-Wavelet للتنبؤ بالتقلبات
        - تحليل علاقات التكامل المشترك متعدد المستويات
        - استخدام تحليل المويجات في اختبارات السببية
        """)

	with col2:
		st.markdown("### تطبيقات في التحليل المالي والاقتصادي")
		st.markdown("""
        - تحليل أسواق الأسهم والسندات باستخدام تقنيات Wavelet
        - دراسة العلاقات بين أسواق العملات باستخدام تماسك المويجات
        - تحليل دورات الأعمال والعلاقات الاقتصادية متعددة المستويات
        - تقنيات Wavelet في تحليل أسعار السلع والطاقة
        - الكشف عن الأزمات المالية والعدوى باستخدام المويجات
        """)

		st.markdown("### الخوارزميات المتقدمة والتنفيذ")
		st.markdown("""
        - تنفيذ تحويلات المويجات في R و Python و MATLAB
        - تقنيات تقليل الضوضاء (Denoising) باستخدام المويجات
        - طرق مبتكرة لتحليل السلاسل الزمنية غير المستقرة
        - نماذج التنبؤ الهجينة باستخدام Wavelet والتعلم الآلي
        - أدوات تصور نتائج تحليل المويجات
        """)

	# Sample wavelet visualization using Plotly
	st.markdown("### مثال توضيحي: تحليل المويجات لبيانات اقتصادية")

	# Create a simple plot to demonstrate (normally this would use real data)
	# Sample time series data
	t_np = np.linspace(0, 5, 1000)
	s1_np = np.sin(5 * np.pi * t_np) + np.sin(10 * np.pi * t_np) + 0.5 * np.random.randn(len(t_np))

	# Simulated wavelet scalogram data
	freq_np = np.linspace(1, 20, 100)
	time_np = np.linspace(0, 5, 200)
	power_np = np.zeros((len(freq_np), len(time_np)))

	for i, f_val in enumerate(freq_np):
		for j, tt_val in enumerate(time_np):
			power_np[i, j] = np.abs(np.sin(f_val * tt_val)) + 0.2 * np.random.rand()

	# Create Plotly figure with subplots
	fig_plotly = make_subplots(
		rows=2, cols=1,
		subplot_titles=(
			'سلسلة زمنية اقتصادية (بيانات توضيحية)',
			'تحليل المويجات (Scalogram توضيحي)'
		),
		vertical_spacing=0.15
	)

	# Time domain plot
	fig_plotly.add_trace(
		go.Scatter(x=t_np, y=s1_np, mode='lines', name='السلسلة الزمنية'),
		row=1, col=1
	)

	# Plot scalogram (Heatmap)
	fig_plotly.add_trace(
		go.Heatmap(
			z=power_np,
			x=time_np,
			y=freq_np,
			colorscale='Viridis',
			colorbar_title_text='الطاقة'
		),
		row=2, col=1
	)

	# Update x and y axis titles for each subplot
	fig_plotly.update_xaxes(title_text='الزمن', row=1, col=1)
	fig_plotly.update_yaxes(title_text='القيمة', row=1, col=1)
	fig_plotly.update_xaxes(title_text='الزمن', row=2, col=1)
	fig_plotly.update_yaxes(title_text='التردد', row=2, col=1)

	fig_plotly.update_layout(
		height=700,
		showlegend=False,
		margin=dict(l=50, r=50, t=80, b=80)  # Adjust margins
	)

	st.plotly_chart(fig_plotly, use_container_width=True)

	st.markdown("""
    يوضح الرسم البياني أعلاه مثالاً توضيحياً لتحليل المويجات، حيث يظهر:

    1. **السلسلة الزمنية الأصلية**: تمثل بيانات اقتصادية أو مالية مثل أسعار الأسهم، معدلات الصرف، أو مؤشرات اقتصادية.

    2. **مخطط المويجات (Scalogram)**: يوضح توزيع طاقة الإشارة عبر الزمن والتردد، مما يكشف عن:
       - الدورات قصيرة المدى وطويلة المدى في البيانات
       - التغيرات الهيكلية والانتقالات
       - العلاقات متعددة المستويات بين المتغيرات الاقتصادية

    في الدورة، ستتعلم كيفية إجراء هذه التحليلات على بيانات حقيقية وتفسير النتائج لاستخلاص رؤى اقتصادية قيمة.
    """)

	st.markdown("---")

	st.markdown("### ميزات تقنيات Wavelet في القياس الاقتصادي")

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("""
        ✅ **تحليل متعدد المستويات**: القدرة على دراسة العلاقات الاقتصادية على مستويات مختلفة (قصيرة، متوسطة، طويلة المدى).

        ✅ **معالجة عدم الاستقرار**: أداء أفضل مع السلاسل الزمنية غير المستقرة مقارنة بالتقنيات التقليدية.

        ✅ **كشف التغيرات الهيكلية**: تحديد نقاط التحول والتغيرات الهيكلية في الأنظمة الاقتصادية.
        """)

	with col2:
		st.markdown("""
        ✅ **تحليل العلاقات المتغيرة زمنياً**: دراسة كيفية تطور العلاقات بين المتغيرات الاقتصادية عبر الزمن.

        ✅ **دقة تنبؤ محسنة**: تحسين دقة نماذج التنبؤ الاقتصادي والمالي من خلال الدمج مع تقنيات Wavelet.

        ✅ **تصور متقدم**: أدوات تصور قوية لفهم الأنماط المعقدة في البيانات الاقتصادية.
        """)

	st.info(
		"في هذه الدورة، ستتعلم كيفية تطبيق تقنيات Wavelet على مجموعة واسعة من المشكلات الاقتصادية والمالية، مع التركيز على التنفيذ العملي باستخدام R و Python و MATLAB.")

elif st.session_state.nav == "البرمجيات":
	st.title("التدريب على البرمجيات الإحصائية")

	st.markdown("""
    تتضمن الدورة تدريباً شاملاً على مجموعة متنوعة من البرمجيات الإحصائية المستخدمة في القياس الاقتصادي.
    سيكتسب المشاركون مهارات عملية في خمس منصات برمجية رئيسية، مما يمكنهم من اختيار الأداة المناسبة
    للمهمة التحليلية المطلوبة.
    """)

	tab1, tab2, tab3, tab4, tab5 = st.tabs(["R", "Python", "MATLAB", "Stata", "EViews"])

	with tab1:
		col1, col2 = st.columns([2, 1])

		with col1:
			st.markdown("## R")
			st.markdown("""
            لغة برمجة قوية للحوسبة الإحصائية وتصور البيانات، مع مجموعة واسعة من الحزم المتخصصة للقياس الاقتصادي.

            ### التطبيقات الرئيسية:
            - الحوسبة الإحصائية المتقدمة
            - تصور البيانات عالي الجودة
            - حزم متخصصة للقياس الاقتصادي

            ### الحزم التي سيتم تغطيتها:
            - **lmtest, sandwich**: للانحدار المتقدم واختبارات التشخيص
            - **tseries, forecast, fGarch**: لتحليل السلاسل الزمنية
            - **plm, pglm**: لنماذج البيانات الطولية
            - **spatialreg, spdep**: للقياس الاقتصادي المكاني
            - **waveslim, wavelets, WaveletComp**: لتحليل المويجات
            - **text2vec, quanteda, topicmodels**: لتحليل النصوص
            - **glmnet, randomForest, xgboost**: للتعلم الآلي
            - **MCMCpack, R2jags**: للقياس الاقتصادي البايزي
            """)

		with col2:
			# Placeholder for R logo or code example
			st.markdown("### مثال كود R")
			st.code("""
# تحليل نموذج GARCH مع R
library(fGarch)

# تقدير نموذج GARCH(1,1)
garch_model <- garchFit(
  formula = ~ garch(1, 1), 
  data = returns,
  trace = FALSE
)

# ملخص النموذج
summary(garch_model)

# التنبؤ
garch_forecast <- predict(
  garch_model, 
  n.ahead = 10
)
            """)

	with tab2:
		col1, col2 = st.columns([2, 1])

		with col1:
			st.markdown("## Python")
			st.markdown("""
            لغة برمجة متعددة الاستخدامات مع مكتبات قوية لتحليل البيانات، التعلم الآلي، ومعالجة اللغة الطبيعية.

            ### التطبيقات الرئيسية:
            - تطبيقات التعلم الآلي
            - تحليل البيانات الضخمة
            - استخراج النصوص
            - استخراج البيانات من الويب

            ### المكتبات التي سيتم تغطيتها:
            - **NumPy, Pandas**: للتعامل مع البيانات وتحليلها
            - **Statsmodels**: لنماذج القياس الاقتصادي التقليدية
            - **Scikit-learn**: لخوارزميات التعلم الآلي
            - **PyWavelets**: لتحليل المويجات
            - **NLTK, Gensim, spaCy**: لمعالجة اللغة الطبيعية
            - **TensorFlow, PyTorch**: للتعلم العميق
            - **pmdarima, Prophet**: للتنبؤ بالسلاسل الزمنية
            - **PySAL**: للتحليل المكاني
            """)

		with col2:
			# Placeholder for Python logo or code example
			st.markdown("### مثال كود Python")
			st.code("""
# تحليل VAR مع Python
import pandas as pd
import numpy as np
from statsmodels.tsa.api import VAR

# تقدير نموذج VAR
model = VAR(data)
results = model.fit(maxlags=5, 
                    ic='aic')

# ملخص النموذج
print(results.summary())

# تحليل دالة الاستجابة النبضية
irf = results.irf(10)
irf.plot(orth=True)
            """)

	with tab3:
		col1, col2 = st.columns([2, 1])

		with col1:
			st.markdown("## MATLAB")
			st.markdown("""
            بيئة برمجية قوية تتفوق في العمليات المصفوفية، التحسين، والمحاكاة.

            ### التطبيقات الرئيسية:
            - العمليات المصفوفية
            - التحسين
            - المحاكاة
            - النمذجة المالية

            ### الأدوات والصناديق التي سيتم تغطيتها:
            - **Econometrics Toolbox**: للقياس الاقتصادي التقليدي
            - **Financial Toolbox**: للتحليل المالي
            - **Statistics and Machine Learning Toolbox**: للإحصاء والتعلم الآلي
            - **Wavelet Toolbox**: لتحليل المويجات
            - **Optimization Toolbox**: لتحسين النماذج
            - **DSGE Tools**: لنماذج التوازن العام الديناميكي العشوائي
            - **Spatial Econometrics Toolbox**: للقياس الاقتصادي المكاني
            """)

		with col2:
			# Placeholder for MATLAB logo or code example
			st.markdown("### مثال كود MATLAB")
			st.code("""
% تقدير نموذج VECM في MATLAB
% تحديد عدد المتغيرات الداخلية
nvar = 3;  

% إنشاء نموذج VECM
vecm_model = vecm(nvar, 'Rank', 1, ...
    'Trend', 'Constant', ... % Example, adjust as needed
    'NumLags', 2); % Example, adjust as needed


% تقدير النموذج
[EstVECM, EstSE, LogLik, E] = estimate(vecm_model, data);


% عرض ملخص النموذج
summarize(EstVECM)
            """)  # Corrected MATLAB example slightly

	with tab4:
		col1, col2 = st.columns([2, 1])

		with col1:
			st.markdown("## Stata")
			st.markdown("""
            برنامج إحصائي شامل مع واجهة سهلة الاستخدام ومخرجات جاهزة للنشر.

            ### التطبيقات الرئيسية:
            - تحليل البيانات الطولية
            - تحليل بيانات المسح
            - تأثيرات المعالجة
            - مخرجات جاهزة للنشر

            ### الأوامر والوحدات التي سيتم تغطيتها:
            - **regress, xtreg, xtlogit**: للانحدار وتحليل البيانات الطولية
            - **arima, var, vecm**: لنماذج السلاسل الزمنية
            - **arch, garch**: لنماذج التقلب
            - **spatreg, spmap**: للقياس الاقتصادي المكاني
            - **psmatch2, teffects**: لتقدير تأثيرات المعالجة
            - **lasso, elasticnet**: للانحدار المنتظم
            - **wavelet**: لتحليل المويجات (وحدة خارجية)
            - **bayes**: للقياس الاقتصادي البايزي
            """)

		with col2:
			# Placeholder for Stata logo or code example
			st.markdown("### مثال كود Stata")
			st.code("""
* تحليل البيانات الطولية في Stata
* نموذج التأثيرات الثابتة
xtreg y x1 x2 x3, fe

* نموذج التأثيرات العشوائية
xtreg y x1 x2 x3, re

* اختبار Hausman
hausman fixed random

* نموذج GMM للبيانات الطولية الديناميكية
xtabond2 y L.y x1 x2 x3, ///
  gmmstyle(L.y, laglimits(1 2)) ///
  ivstyle(x1 x2 x3) twostep robust
            """)  # Corrected Stata example slightly

	with tab5:
		col1, col2 = st.columns([2, 1])

		with col1:
			st.markdown("## EViews")
			st.markdown("""
            برنامج متخصص في تحليل السلاسل الزمنية والتنبؤ، مع واجهة مستخدم سهلة الاستخدام.

            ### التطبيقات الرئيسية:
            - تحليل السلاسل الزمنية
            - التنبؤ
            - تحليل دورة الأعمال
            - نمذجة GARCH

            ### الميزات والأدوات التي سيتم تغطيتها:
            - **نماذج ARIMA و SARIMA**: للسلاسل الزمنية أحادية المتغير
            - **VAR و VECM**: للسلاسل الزمنية متعددة المتغيرات
            - **ARCH و GARCH**: لنماذج التقلب
            - **SSpace**: لنماذج الحالة المكانية
            - **Panel**: لتحليل البيانات الطولية
            - **Frequency Domain Analysis**: لتحليل المجال الترددي والمويجات
            - **Automated Forecasting**: للتنبؤ الآلي
            """)

		with col2:
			# Placeholder for EViews logo or code example
			st.markdown("### مثال كود EViews")
			st.code("""
' تقدير نموذج ARIMA في EViews
' إنشاء نموذج ARIMA(2,1,2)
equation arima_eq.ls d(y) c ar(1) ar(2) ma(1) ma(2)

' الاحصاءات التشخيصية
arima_eq.makeresids resid_arima
show resid_arima.correl(36)
show resid_arima.hist

' التنبؤ
arima_eq.forecast y_f
            """)  # Corrected EViews example slightly

	st.markdown("---")

	st.markdown("### مميزات التدريب على البرمجيات")

	col1, col2 = st.columns(2)

	with col1:
		st.markdown("""
        ✅ **تدريب عملي**: ستتعلم من خلال التطبيق العملي على بيانات حقيقية

        ✅ **أكواد جاهزة**: ستحصل على مكتبة من الأكواد الجاهزة للاستخدام في مشاريعك

        ✅ **مقارنة بين البرمجيات**: فهم متى تستخدم كل برنامج ومزاياه النسبية
        """)

	with col2:
		st.markdown("""
        ✅ **تقنيات متقدمة**: تعلم التقنيات المتقدمة مثل البرمجة الموازية وإدارة البيانات الضخمة

        ✅ **دمج البرمجيات**: كيفية دمج مخرجات البرمجيات المختلفة في تحليل متكامل

        ✅ **تخصيص وتوسيع**: كيفية تخصيص وتوسيع البرمجيات لتلبية احتياجاتك الخاصة
        """)

	st.markdown("### محاضرات أساسيات البرمجيات")
	st.markdown("""
    في بداية الدورة، سيتم تقديم محاضرات إضافية عن أساسيات البرمجيات لضمان أن جميع المشاركين
    لديهم المعرفة الأساسية اللازمة للاستفادة القصوى من الدورة. ستغطي هذه المحاضرات:

    - مقدمة أساسية لكل برنامج
    - تنصيب البرامج وإعدادها
    - التعامل مع البيانات (استيراد، تصدير، تنظيف)
    - الأوامر والدوال الأساسية
    - تصور البيانات الأساسي
    """)

elif st.session_state.nav == "التسجيل":
	st.title("التسجيل في دورة القياس الاقتصادي المتقدمة 2025")

	st.markdown("""
    يرجى التسجيل في الدورة من خلال الرابط التالي. بعد إكمال النموذج، سنتواصل معك بخصوص تفاصيل الدفع وجدول الدورة.
    """)

	google_form_link = "https://docs.google.com/forms/d/1jYiS8Ye7yC9u20b6t5prRhzl_Y-PhSz-ykz-LYVK5HU/preview"
	st.markdown(f"### [🔗 اضغط هنا للتسجيل عبر نموذج جوجل 🔗]({google_form_link})", unsafe_allow_html=True)

	st.markdown("---")

	pdf_course_info_link = "https://drive.google.com/file/d/1kD9QNwHgcGWvKIpzC5rDC63a380yfs0B/view?usp=sharing"
	st.markdown(f"""
    ### 📄 للاطلاع على تفاصيل إضافية ومحتوى الدورة
    يمكنك تحميل أو معاينة الملف التعريفي للدورة من خلال الرابط التالي:
    [ملف PDF تعريفي بالدورة]({pdf_course_info_link})
    """)
	st.markdown("")  # Add some space

	st.markdown("---")

	st.markdown("### رسوم الدورة")
	st.markdown("""
    - **الطلاب الدوليين**: $80 USD
    - **الطلاب الجزائريين**: 7,000 DA

    تشمل الرسوم:
    - حضور جميع جلسات الدورة
    - جميع المواد التعليمية والبرمجيات
    - كتاب تفاعلي بتنسيق PDF
    - شهادة معتمدة عند إكمال الدورة
    - دورة مجانية للمبتدئين (حسب الحاجة)
    """)

	st.markdown("### طرق الدفع")
	st.markdown("""
    بعد التسجيل عبر النموذج، سنرسل إليك تفاصيل طرق الدفع المتاحة، والتي تشمل:
    - التحويل المصرفي
    - الدفع الإلكتروني
    - خيارات أخرى حسب البلد
    """)

elif st.session_state.nav == "الأسئلة الشائعة":
	st.title("الأسئلة الشائعة")

	faq_data = [
		{
			"question": "متى تبدأ الدورة؟",
			"answer": "ستبدأ الدورة عندما يتم الوصول إلى الحد الأدنى من المشاركين. سيتم إعلام جميع المسجلين بتاريخ البدء المحدد عبر البريد الإلكتروني."
		},
		{
			"question": "ما هي المتطلبات الأساسية للدورة؟",
			"answer": "يفضل أن يكون لديك معرفة أساسية بالإحصاء والاقتصاد، ولكن ليست ضرورية حيث سنقدم دورة مجانية للمبتدئين قبل بداية الدورة الرئيسية. كما يفضل أن يكون لديك جهاز كمبيوتر مع إمكانية تثبيت البرمجيات اللازمة."
		},
		{
			"question": "هل الدورة عبر الإنترنت أم حضورية؟",
			"answer": "الدورة متاحة عبر الإنترنت بشكل افتراضي، مما يتيح المشاركة من أي مكان في العالم. قد تتوفر خيارات الحضور الشخصي في مواقع محددة حسب الطلب."
		},
		{
			"question": "ما هي لغة تقديم الدورة؟",
			"answer": "سيتم تقديم الدورة باللغة العربية، مع توفير المصطلحات التقنية والمراجع باللغة الإنجليزية أيضاً."
		},
		{
			"question": "هل سأحصل على شهادة بعد إكمال الدورة؟",
			"answer": "نعم، ستحصل على شهادة معتمدة بعد إكمال الدورة بنجاح، والتي يمكن إضافتها إلى سيرتك الذاتية."
		},
		{
			"question": "هل أحتاج إلى شراء البرمجيات للمشاركة في الدورة؟",
			"answer": "لا، سنعتمد بشكل أساسي على البرمجيات المفتوحة المصدر مثل R و Python، والتي يمكن تحميلها مجاناً. بالنسبة للبرمجيات التجارية مثل MATLAB و Stata و EViews، سنوفر إرشادات للحصول على إصدارات تجريبية أو إصدارات للطلاب."
		},
		{
			"question": "ما هو الوقت المتوقع للدراسة أسبوعياً؟",
			"answer": "تتضمن الدورة ثلاث جلسات أسبوعياً، بالإضافة إلى وقت للتطبيق العملي. يُنصح بتخصيص حوالي 8-10 ساعات أسبوعياً للدراسة والتطبيق."
		},
		{
			"question": "هل يمكنني التركيز على موضوعات محددة؟",
			"answer": "نعم، النموذج المرفق في رابط التسجيل يتضمن خانة لتحديد النماذج والموضوعات التي ترغب في التركيز عليها، وسنحاول تخصيص محتوى الدورة لتلبية هذه الاحتياجات قدر الإمكان."
		},
		{
			"question": "هل سيتم تسجيل الجلسات؟",
			"answer": "نعم، سيتم تسجيل جميع الجلسات وستكون متاحة للمشاركين للرجوع إليها لاحقاً."
		},
		{
			"question": "ما هي سياسة استرداد الرسوم؟",
			"answer": "يمكن استرداد الرسوم بالكامل إذا تم الإلغاء قبل بدء الدورة. بعد بدء الدورة، سيتم تقييم طلبات الاسترداد على أساس كل حالة على حدة."
		}
	]

	for i, faq in enumerate(faq_data):
		with st.expander(f"{i + 1}. {faq['question']}"):
			st.markdown(faq['answer'])

	st.markdown("---")

	st.markdown("### هل لديك سؤال آخر؟")
	question = st.text_area("اكتب سؤالك هنا وسنرد عليك في أقرب وقت ممكن", height=100)
	contact_email = st.text_input("البريد الإلكتروني للتواصل")

	if st.button("إرسال السؤال"):
		if question and contact_email:
			# Here you would typically send an email or save the question to a database.
			# For this example, we'll just show a success message.
			st.success("تم إرسال سؤالك بنجاح! سنرد عليك قريباً عبر البريد الإلكتروني.")
		else:
			st.error("يرجى كتابة سؤالك وإدخال بريدك الإلكتروني.")

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p>© 2025 دورة القياس الاقتصادي المتقدمة - د. مروان رودان</p>
    <p>للتواصل: course2025a@gmail.com</p>
</div>
""", unsafe_allow_html=True)
