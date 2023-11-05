interface Item {
    company?: string; // Use ? for optional properties if not all your items have a company
    name: string;
    price: string;
    imagePath: string;
}

async function fetchData() {
    try {
        // Replace with '/api/products' or '/api/restaurants' as necessary
        const response = await fetch('http://127.0.0.1:5000/api/products');
        const items: Item[] = await response.json();
        displayItems(items);
    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

function displayItems(items: Item[]) {
    const itemsContainer: HTMLElement | null = document.getElementById('items-container');
    if (itemsContainer) {
        itemsContainer.innerHTML = ''; // Clear out any existing content
        items.forEach((item) => {
            const itemCard = `
                <div class="card">
                    <img src="${item.imagePath}" alt="${item.name}" />
                    <div class="card-body">
                        <h3 class="card-title">${item.name}</h3>
                        <p class="card-text">${item.company || ''}</p>
                        <p class="price">$${item.price}</p>
                    </div>
                </div>
            `;
            itemsContainer.innerHTML += itemCard; // Append new card
        });
    }
}

fetchData();

