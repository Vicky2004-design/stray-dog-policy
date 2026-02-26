import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set font for Traditional Chinese (Noto Sans CJK TC)
font_path = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
if not os.path.exists(font_path):
    # Fallback to any available font if the specific one is not found
    font_prop = fm.FontProperties(size=12)
else:
    font_prop = fm.FontProperties(fname=font_path, size=12)

# Data for the comparison table
countries = ['新加坡', '德國', '荷蘭', '臺灣']
categories = ['核心策略', '成功因素', '借鏡重點']

data = {
    '新加坡': {
        '核心策略': 'TNRM\n制度化管理遊蕩犬',
        '成功因素': '• 政府與跨部門合作\n• 八成遊蕩犬完成絕育\n• 公眾教育與志工長期管理',
        '借鏡重點': 'TNR 必須「有管理」\n結合登記與社區參與\n避免「只放不管」導致問題回流'
    },
    '德國': {
        '核心策略': '源頭零漏洞\n高度管控體系',
        '成功因素': '• 強制晶片 + 登記制\n• 嚴格法律與高額罰金\n• 將犬隻視為家庭成員',
        '借鏡重點': '源頭零漏洞的責任制度\n透過強制晶片、登記與高額罰則\n從源頭阻斷浪犬產生'
    },
    '荷蘭': {
        '核心策略': '2019實施零流浪犬',
        '成功因素': '• 強制登記 + 養狗稅\n• 高額罰款與監禁\n• 經濟與社福基礎高',
        '借鏡重點': '多管齊下治理\n結合法律、經濟、教育與文化\n全面強化飼主責任'
    },
    '臺灣': {
        '核心策略': '零撲殺配套不足',
        '成功因素': '• 不當餵食問題嚴重\n• 棄養未根除\n• 遊蕩犬數量仍高',
        '借鏡重點': '必須多管齊下\n絕育、教育、登記、重罰\n缺一不可'
    }
}

# Create the figure
fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
ax.axis('off')

# Table settings
n_rows = len(categories) + 1
n_cols = len(countries) + 1
row_height = 1.0 / n_rows
col_width = 1.0 / n_cols

# Draw background and headers
for i, country in enumerate(countries):
    # Header background
    rect = plt.Rectangle(( (i+1)*col_width, 1-row_height ), col_width, row_height, facecolor='#333333', edgecolor='white', linewidth=1)
    ax.add_patch(rect)
    # Header text
    ax.text((i+1.5)*col_width, 1-0.5*row_height, country, color='white', ha='center', va='center', fontproperties=font_prop, fontweight='bold', fontsize=14)

for j, category in enumerate(categories):
    # Category background
    rect = plt.Rectangle(( 0, 1-(j+2)*row_height ), col_width, row_height, facecolor='#f2f2f2', edgecolor='white', linewidth=1)
    ax.add_patch(rect)
    # Category text
    ax.text(0.5*col_width, 1-(j+1.5)*row_height, category, color='#333333', ha='center', va='center', fontproperties=font_prop, fontweight='bold', fontsize=12)

# Fill data cells
for i, country in enumerate(countries):
    for j, category in enumerate(categories):
        content = data[country][category]
        # Cell background
        rect = plt.Rectangle(( (i+1)*col_width, 1-(j+2)*row_height ), col_width, row_height, facecolor='white', edgecolor='#e0e0e0', linewidth=0.5)
        ax.add_patch(rect)
        # Cell text
        # Adjust text position for better padding and readability
        text_x = (i+1)*col_width + 0.015
        text_y = 1-(j+1.5)*row_height
        ax.text(text_x, text_y, content, color='#333333', ha='left', va='center', fontproperties=font_prop, fontsize=10.5, wrap=True, linespacing=1.6)

# Add title
plt.text(0.5, 1.05, '各國遊蕩犬管理政策對比分析', ha='center', va='bottom', fontproperties=font_prop, fontsize=18, fontweight='bold', transform=ax.transAxes)

# Save the plot
plt.savefig('/home/ubuntu/stray_dog_policy/pro_comparison_academic.png', bbox_inches='tight', pad_inches=0.5)
print("Professional academic infographic generated successfully.")
