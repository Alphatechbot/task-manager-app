<script>
    // Toggle between login and task list page after login (simple demo logic)
    document.querySelector('form[action="/login/"]').onsubmit = function(event) {
        event.preventDefault();  // Replace this with actual login process via Django backend
        document.getElementById('loginForm').style.display = 'none';
        document.getElementById('todoApp').style.display = 'block';
    };

    // Sample task management (CRUD)
    const taskList = document.getElementById('taskList');
    const addTaskForm = document.getElementById('addTaskForm');
    const newTaskInput = document.getElementById('newTask');

    let tasks = [];

    // Add Task
    addTaskForm.onsubmit = function(event) {
        event.preventDefault();
        const taskText = newTaskInput.value.trim();
        if (taskText !== '') {
            const taskId = tasks.length;
            tasks.push({ id: taskId, text: taskText, completed: false });
            newTaskInput.value = '';
            renderTasks();
        }
    };

    // Update Task
    function updateTask(taskId, newText) {
        tasks = tasks.map(task => task.id === taskId ? { ...task, text: newText } : task);
        renderTasks();
    }

    // Delete Task
    function deleteTask(taskId) {
        tasks = tasks.filter(task => task.id !== taskId);
        renderTasks();
    }

    // Render Tasks
    function renderTasks() {
        taskList.innerHTML = '';
        tasks.forEach(task => {
            const li = document.createElement('li');
            li.className = 'task';
            li.innerHTML = `
                <input type="text" value="${task.text}" onchange="updateTask(${task.id}, this.value)">
                <button onclick="deleteTask(${task.id})">Delete</button>
            `;
            taskList.appendChild(li);
        });
    }
    function showEditForm(taskId) {
    document.getElementById('edit-form-' + taskId).style.display = 'flex';
    }

    function hideEditForm(taskId) {
        document.getElementById('edit-form-' + taskId).style.display = 'none';
    }

    function saveTask(taskId) {
        // Logic for saving the task goes here (you'll handle this with Django).
        const newTaskName = document.getElementById('edit-input-' + taskId).value;
        // Example of updating the task name visually after saving
        document.querySelector('#task-' + taskId + ' .task-name').innerText = newTaskName;
        hideEditForm(taskId);
    }


</script>
