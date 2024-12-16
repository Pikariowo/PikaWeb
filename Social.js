const fetchButton = document.getElementById('fetchButton');
const postContainer = document.getElementById('postContainer');

const API_URL = 'https://jsonplaceholder.typicode.com/posts/10';

//API
fetchButton.addEventListener('click', () => {
    fetch(API_URL) // 發送 GET 請求
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json(); // 將響應解析為 JSON
        })
        .then(data => {
            // 顯示 API 的資料
            postContainer.innerHTML = `
                <h2>${data.title}</h2>
                <p>Id：${data.id}</p> 
                <p>${data.body}</p>                           
            `;
        })
        .catch(error => {
            postContainer.innerHTML = `<p style="color: red;">錯誤：${error.message}</p>`;
        });
});
