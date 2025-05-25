// メインJavaScriptファイル

/**
 * DOMが読み込まれた後に実行される初期化関数
 */
document.addEventListener('DOMContentLoaded', function() {
    console.log('Joycon Action アプリが初期化されました');
    
    // アニメーション効果の初期化
    initializeAnimations();
    
    // カスタムイベントリスナーの設定
    setupEventListeners();
});

/**
 * アニメーション効果を初期化
 */
function initializeAnimations() {
    // フェードインアニメーションを適用
    const elements = document.querySelectorAll('.card, .welcome-message');
    elements.forEach((element, index) => {
        setTimeout(() => {
            element.classList.add('fade-in');
        }, index * 100);
    });
}

/**
 * カスタムイベントリスナーを設定
 */
function setupEventListeners() {
    // Streamlitイベントのリスナー
    document.addEventListener('streamlit:render', function() {
        console.log('Streamlitが再レンダリングされました');
        initializeAnimations();
    });
    
    // カスタムボタンのクリックイベント
    const customButtons = document.querySelectorAll('.custom-button');
    customButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // ボタンクリック時のエフェクト
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

/**
 * ローディング表示を切り替え
 * @param {boolean} show - 表示するかどうか
 */
function toggleLoading(show) {
    let loader = document.getElementById('custom-loader');
    
    if (show) {
        if (!loader) {
            loader = document.createElement('div');
            loader.id = 'custom-loader';
            loader.className = 'loader';
            document.body.appendChild(loader);
        }
        loader.style.display = 'block';
    } else {
        if (loader) {
            loader.style.display = 'none';
        }
    }
}

/**
 * 通知メッセージを表示
 * @param {string} message - メッセージ
 * @param {string} type - タイプ ('success', 'error', 'info')
 */
function showNotification(message, type = 'info') {
    // Streamlitの通知システムを使用
    if (window.streamlit) {
        const notification = {
            message: message,
            type: type
        };
        
        // カスタムイベントを発火
        const event = new CustomEvent('customNotification', { 
            detail: notification 
        });
        document.dispatchEvent(event);
    } else {
        // フォールバック: ブラウザのアラート
        alert(message);
    }
}

/**
 * データをローカルストレージに保存
 * @param {string} key - キー
 * @param {any} data - データ
 */
function saveToLocalStorage(key, data) {
    try {
        localStorage.setItem(key, JSON.stringify(data));
        return true;
    } catch (error) {
        console.error('ローカルストレージへの保存に失敗:', error);
        return false;
    }
}

/**
 * ローカルストレージからデータを読み込み
 * @param {string} key - キー
 * @returns {any} データ
 */
function loadFromLocalStorage(key) {
    try {
        const data = localStorage.getItem(key);
        return data ? JSON.parse(data) : null;
    } catch (error) {
        console.error('ローカルストレージからの読み込みに失敗:', error);
        return null;
    }
}

/**
 * 日時を日本語形式でフォーマット
 * @param {Date} date - 日時オブジェクト
 * @returns {string} フォーマットされた日時文字列
 */
function formatDateJapanese(date = new Date()) {
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        timeZone: 'Asia/Tokyo'
    };
    
    return new Intl.DateTimeFormat('ja-JP', options).format(date);
}

/**
 * ページの表示状態を監視
 */
function setupPageVisibilityListener() {
    document.addEventListener('visibilitychange', function() {
        if (document.hidden) {
            console.log('ページが非表示になりました');
        } else {
            console.log('ページが表示されました');
            // ページが再表示された際の処理
            initializeAnimations();
        }
    });
}

// ページ表示状態の監視を開始
setupPageVisibilityListener();

// エクスポート（モジュール環境での使用のため）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        toggleLoading,
        showNotification,
        saveToLocalStorage,
        loadFromLocalStorage,
        formatDateJapanese
    };
}