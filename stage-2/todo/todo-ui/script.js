API_URL = "http://localhost:8000/"

async function get_all_tasks() {
    const response = await fetch(API_URL + "tasks/");
    const tasks = await response.json();

    return tasks;
}

async function print_all_tasks() {
    const tasks = await get_all_tasks();
    const container = document.getElementById("tasks-list");

    for (task of tasks) {
        const content = `
            <div class="task-item">
                <input type="checkbox">${task.title}
            </div>
        `;

        container.innerHTML += content;
    }
}

document.querySelector("#new-task").addEventListener("submit", function (event) {
    event.preventDefault();

    var form = event.target;
    var formData = new FormData(form);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:8000/task/create/", true);
    xhr.send(formData);

    location.reload();
});

print_all_tasks()