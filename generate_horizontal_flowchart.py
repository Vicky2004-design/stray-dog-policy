import graphviz

def generate_horizontal_flowchart():
    # 建立橫式流程圖 (Rankdir='LR')
    dot = graphviz.Digraph(comment='Taiwan Stray Dog Policy Flowchart Horizontal', format='png')
    dot.attr(rankdir='LR', size='16,10', dpi='300', ranksep='0.8', nodesep='0.5')
    dot.attr('node', fontname='Noto Sans TC', shape='box', style='rounded,filled', fillcolor='#ffffff', color='#1a1a1a', penwidth='1.5', margin='0.2,0.1')
    dot.attr('edge', fontname='Noto Sans TC', color='#1a1a1a', penwidth='1.2', fontsize='10')

    # 定義節點
    dot.node('start', '🐶 通報／巡查發現遊蕩犬', shape='capsule', fillcolor='#1a1a1a', fontcolor='#ffffff')
    dot.node('policy', '管理政策時期', shape='diamond')
    
    # 零撲殺前路徑
    dot.node('catch_all', '無差別捕捉')
    dot.node('shelter_before', '送往收容所')
    dot.node('adopt_check', '有人領回或送養？', shape='diamond')
    dot.node('leave_shelter', '✅ 離所 (領回/送養)', fillcolor='#1b5e20', fontcolor='#ffffff')
    dot.node('euthanasia', '❌ 撲殺 (安樂死)', fillcolor='#ffffff', fontcolor='#d32f2f', color='#d32f2f')

    # 零撲殺後路徑
    dot.node('risk_eval', '行為風險評估', shape='diamond')
    
    # 高風險
    dot.node('high_risk', '⚠️ 高風險個體', fillcolor='#fff3cd', color='#fbc02d')
    dot.node('precise_catch', '精準捕捉')
    dot.node('remove_env', '帶離環境')
    dot.node('long_shelter', '🏠 不回置 (收容/安置)', fillcolor='#1a1a1a', fontcolor='#ffffff')
    
    # 一般
    dot.node('normal', '✅ 一般遊蕩犬', fillcolor='#e8f5e9', color='#2e7d32')
    dot.node('tnvr_flow', '💜 TNVR 流程', fillcolor='#f3e5f5', color='#7b1fa2')
    dot.node('trap', '誘捕 Trap')
    dot.node('neuter', '結紮 Neuter')
    dot.node('vaccinate', '疫苗 Vaccinate')
    dot.node('return', '回置 Return')
    dot.node('goal', '🎯 目標：族群控制與免疫', shape='capsule', fillcolor='#1a1a1a', fontcolor='#ffffff')

    # 建立連接
    dot.edge('start', 'policy')
    
    # 零撲殺前
    dot.edge('policy', 'catch_all', label='零撲殺前')
    dot.edge('catch_all', 'shelter_before')
    dot.edge('shelter_before', 'adopt_check')
    dot.edge('adopt_check', 'leave_shelter', label='是')
    dot.edge('adopt_check', 'euthanasia', label='否')
    
    # 零撲殺後
    dot.edge('policy', 'risk_eval', label='零撲殺後')
    dot.edge('risk_eval', 'high_risk', label='高風險')
    dot.edge('high_risk', 'precise_catch')
    dot.edge('precise_catch', 'remove_env')
    dot.edge('remove_env', 'long_shelter')
    
    dot.edge('risk_eval', 'normal', label='一般')
    dot.edge('normal', 'tnvr_flow')
    dot.edge('tnvr_flow', 'trap')
    dot.edge('trap', 'neuter')
    dot.edge('neuter', 'vaccinate')
    dot.edge('vaccinate', 'return')
    dot.edge('return', 'goal')

    # 渲染圖片
    dot.render('/home/ubuntu/stray_dog_policy/flowchart_horizontal', cleanup=True)
    print("Horizontal flowchart generated successfully at /home/ubuntu/stray_dog_policy/flowchart_horizontal.png")

if __name__ == "__main__":
    generate_horizontal_flowchart()
