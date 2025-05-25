import streamlit as st
from datetime import datetime

def hello_world_component():
    """
    Hello Worldメッセージを表示するコンポーネント
    
    このコンポーネントは：
    - 歓迎メッセージを表示
    - 現在の日時を表示
    - インタラクティブな要素を含む
    """
    
    # メインのHello Worldメッセージ
    st.markdown("""
    <div class="welcome-message">
        <h2 style="text-align: center; color: #2e7d32;">🌟 Hello World! 🌟</h2>
        <p style="text-align: center; font-size: 18px;">
            Streamlitアプリケーションへようこそ！
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 現在時刻の表示
    current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
    st.write(f"**現在時刻:** {current_time}")
    
    # インタラクティブな要素
    st.subheader("インタラクティブなHello World")
    
    # ユーザー名入力
    user_name = st.text_input("お名前を入力してください:", placeholder="山田太郎")
    
    if user_name:
        st.balloons()  # アニメーション効果
        st.success(f"こんにちは、{user_name}さん！ 🎉")
        
        # パーソナライズされたメッセージ
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("👋 挨拶"):
                st.write(f"Hello, {user_name}!")
        
        with col2:
            if st.button("🎵 応援"):
                st.write(f"がんばって、{user_name}さん！")
        
        with col3:
            if st.button("🌟 褒める"):
                st.write(f"素晴らしいですね、{user_name}さん！")
    
    # 追加のデモ機能
    st.subheader("デモ機能")
    
    # スライダー
    number = st.slider("数値を選択してください", 1, 100, 50)
    st.write(f"選択された数値: **{number}**")
    
    # プログレスバー
    if st.button("プログレスバーのデモ"):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
        st.success("完了！")
    
    # チャート表示のデモ
    st.subheader("チャートデモ")
    import numpy as np
    import pandas as pd
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)