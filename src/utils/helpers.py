"""
ヘルパー関数とユーティリティ
"""

import streamlit as st
from datetime import datetime
import json

def format_datetime(dt=None, format_str="%Y年%m月%d日 %H:%M:%S"):
    """
    日時をフォーマットして返す
    
    Args:
        dt: datetime object (None の場合は現在時刻)
        format_str: フォーマット文字列
    
    Returns:
        str: フォーマットされた日時文字列
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(format_str)

def load_config(config_path="config.json"):
    """
    設定ファイルを読み込む
    
    Args:
        config_path: 設定ファイルのパス
    
    Returns:
        dict: 設定データ
    """
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.warning(f"設定ファイル {config_path} が見つかりません")
        return {}
    except json.JSONDecodeError:
        st.error(f"設定ファイル {config_path} の形式が正しくありません")
        return {}

def save_config(config_data, config_path="config.json"):
    """
    設定ファイルに保存する
    
    Args:
        config_data: 保存する設定データ
        config_path: 設定ファイルのパス
    """
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        st.error(f"設定の保存に失敗しました: {e}")
        return False

def show_error(message, details=None):
    """
    エラーメッセージを表示する
    
    Args:
        message: エラーメッセージ
        details: 詳細情報（オプション）
    """
    st.error(message)
    if details:
        with st.expander("詳細を表示"):
            st.write(details)

def show_success(message, details=None):
    """
    成功メッセージを表示する
    
    Args:
        message: 成功メッセージ
        details: 詳細情報（オプション）
    """
    st.success(message)
    if details:
        with st.expander("詳細を表示"):
            st.write(details)

def validate_input(value, input_type="text", required=True, min_length=None, max_length=None):
    """
    入力値のバリデーション
    
    Args:
        value: 検証する値
        input_type: 入力タイプ ("text", "email", "number")
        required: 必須かどうか
        min_length: 最小文字数
        max_length: 最大文字数
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if required and not value:
        return False, "この項目は必須です"
    
    if not value:
        return True, None
    
    if input_type == "email":
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, value):
            return False, "有効なメールアドレスを入力してください"
    
    if input_type == "number":
        try:
            float(value)
        except ValueError:
            return False, "数値を入力してください"
    
    if min_length and len(str(value)) < min_length:
        return False, f"{min_length}文字以上で入力してください"
    
    if max_length and len(str(value)) > max_length:
        return False, f"{max_length}文字以下で入力してください"
    
    return True, None