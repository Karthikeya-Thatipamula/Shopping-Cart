function showNotification(message) {
    const notification = document.getElementById('notification');
    if (!notification) {
        console.error('Notification element not found!');
        return;
    }
    notification.textContent = message;
    notification.classList.add('show');
    setTimeout(() => {
        notification.classList.remove('show');
    }, 3000);
}

async function addToCart(product, button) {
    if (button) {
        const originalText = button.textContent;
        button.textContent = 'Adding...';
        button.classList.add('adding');
        button.disabled = true;
    }

    try {
        const response = await fetch('/api/cart', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ product_id: product.id, quantity: 1 }),
        });
        if (response.ok) {
            showNotification('Product added to cart!');
            if (typeof fetchCart === 'function') {
                fetchCart();
            }
        } else if (response.status === 401) {
            showNotification('Please login to add items to your cart.');
        } else {
            const errorData = await response.json();
            showNotification(errorData.message || 'Error adding product to cart.');
        }
    } catch (error) {
        console.error('Add to cart error:', error);
        showNotification('Error adding product to cart.');
    } finally {
        if (button) {
            setTimeout(() => {
                button.textContent = 'Add to Cart';
                button.classList.remove('adding');
                button.disabled = false;
            }, 200);
        }
    }
}
