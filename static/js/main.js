/**
 * Main JavaScript for E-commerce Store
 */

document.addEventListener('DOMContentLoaded', function () {
    initMobileMenu();
    initAutoDismissAlerts();
    initAddToCartFeedback();
    initQuantityValidation();
});

/**
 * Mobile menu toggle
 */
function initMobileMenu() {
    const menuBtn = document.getElementById('mobile-menu-btn');
    const nav = document.querySelector('.nav');

    if (!menuBtn || !nav) return;

    menuBtn.addEventListener('click', function () {
        nav.classList.toggle('active');
        menuBtn.classList.toggle('active');
    });

    document.addEventListener('click', function (e) {
        if (!menuBtn.contains(e.target) && !nav.contains(e.target)) {
            nav.classList.remove('active');
            menuBtn.classList.remove('active');
        }
    });
}

/**
 * Auto-dismiss alert messages after 5 seconds
 */
function initAutoDismissAlerts() {
    const alerts = document.querySelectorAll('[data-auto-dismiss]');

    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            alert.style.transition = 'all 0.3s ease';
            setTimeout(function () {
                alert.remove();
            }, 300);
        }, 5000);
    });
}

/**
 * Visual feedback when adding items to cart
 */
function initAddToCartFeedback() {
    const forms = document.querySelectorAll('.add-to-cart-form, .add-to-cart-detail');

    forms.forEach(function (form) {
        form.addEventListener('submit', function () {
            const btn = form.querySelector('button[type="submit"]');
            if (btn) {
                const originalText = btn.textContent;
                btn.textContent = 'جاري الإضافة...';
                btn.disabled = true;

                setTimeout(function () {
                    btn.textContent = originalText;
                    btn.disabled = false;
                }, 2000);
            }
        });
    });
}

/**
 * Validate quantity inputs against max stock
 */
function initQuantityValidation() {
    const quantityInputs = document.querySelectorAll('.quantity-input');

    quantityInputs.forEach(function (input) {
        input.addEventListener('change', function () {
            const max = parseInt(input.getAttribute('max'), 10);
            const min = parseInt(input.getAttribute('min'), 10) || 1;
            let value = parseInt(input.value, 10);

            if (isNaN(value) || value < min) {
                input.value = min;
            } else if (max && value > max) {
                input.value = max;
            }
        });
    });
}

/**
 * Update cart badge count
 */
function updateCartBadge(count) {
    const badge = document.getElementById('cart-count');
    if (badge) {
        badge.textContent = count;
        badge.style.transform = 'scale(1.3)';
        setTimeout(function () {
            badge.style.transform = 'scale(1)';
            badge.style.transition = 'transform 0.2s ease';
        }, 200);
    }
}
