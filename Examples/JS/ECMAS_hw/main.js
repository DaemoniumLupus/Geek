async function getUserData(userId) {
    try {
        const response = await fetch(`https://api.example.com/users/${userId}`);

        if (!response.ok) {
            throw new Error("User not found");
        }

        const userData = await response.json();
        return userData;
    } catch (error) {
        return Promise.reject(error.message);
    }
}

getUserData(0);

const user = {
    name: 'John Smith',
    age: 30,
    email: 'john@example.com'
};


async function saveUserData(user) {
    try {
        const response = await fetch('https://api.example.com/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(user),
        });
        if (!response.ok) {
            throw new Error('Failed to save user data');
        }
    } catch (error) {
        return Promise.reject(error.message);
    }
}

saveUserData(user);

const el = document.createElement("p");
el.id = 'element';


function changeStyleDelayed(elementId, delay) {
    setTimeout(() => {
        const element = document.getElementById(elementId);
        if (element) {
            element.style.color = 'green';
        }
    }, delay);
}

console.log(el.style);
changeStyleDelayed('element', 2000);
console.log(el.style);
setTimeout(console.log(el.style), 3000);

