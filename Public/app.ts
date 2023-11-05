const message: string = 'Hello, World from Typescript';
console.log(message);

async function fetchData() {
    try {
        // Make sure you use the correct protocol and IP address format
        const response = await fetch('http://127.0.0.1:5000/api/data');
        const data = await response.json();
        console.log(data);
        displayData(data['message']);
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

function displayData(message: string) {
    const appDiv: HTMLElement | null = document.getElementById('app');
    if (appDiv) {
        // Use backticks for template literals
        appDiv.innerHTML = `<h2>${message}</h2>`;
    }
}

fetchData();
