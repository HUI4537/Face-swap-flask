async function startVideo() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        const videoElement = document.getElementById('video');
        videoElement.srcObject = stream;
    } catch (err) {
        console.error('웹캠을 가져오는 동안 오류가 발생했습니다:', err);
    }
}

// 캡처 버튼 클릭 시 호출되는 함수입니다.
function capturePhoto() {
    const videoElement = document.getElementById('video');
    const canvasElement = document.getElementById('canvas');
    const context = canvasElement.getContext('2d');

    // 비디오 화면을 캔버스에 그립니다.
    context.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);

    // 캔버스의 이미지 데이터를 base64 형태로 가져옵니다.
    const imageDataURL = canvasElement.toDataURL('image/jpeg');

    // base64 형태의 이미지를 다운로드할 수 있는 링크를 생성합니다.
    const downloadLink = document.createElement('a');
    downloadLink.href = imageDataURL;
    downloadLink.download = 'captured_photo.jpg';
    downloadLink.click();
}

// 페이지 로드 시 웹캠을 시작합니다.
window.onload = function() {
    startVideo();
    // 캡처 버튼에 클릭 이벤트를 추가합니다.
    document.getElementById('captureButton').addEventListener('click', capturePhoto);
};