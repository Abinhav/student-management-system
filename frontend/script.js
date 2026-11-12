
const API_URL = "http://127.0.0.1:8000";
function showToast(message, type = "success") {
    const toast = document.getElementById("toast");

    toast.textContent = message;
    toast.className = "show";

    if (type === "error") {
        toast.classList.add("error");
    }

    setTimeout(function() {
        toast.className = "";
    }, 3000);
}
const form = document.getElementById("studentForm");
const table = document.getElementById("studentTable");

let editId = null;

async function loadStudents() {
    const response = await fetch(`${API_URL}/students`);
    const students = await response.json();

    table.innerHTML = "";

    students.forEach(student => {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.name}</td>
            <td>${student.age}</td>
            <td>${student.email}</td>
            <td>${student.course}</td>
            <td>
                <button onclick="editStudent(${student.id}, '${encodeURIComponent(JSON.stringify(student))}')">Edit</button>
                <button onclick="deleteStudent(${student.id})">Delete</button>
            </td>
        `;

        table.appendChild(row);
    });
}

form.addEventListener("submit", async function(event) {
    event.preventDefault();

    const student = {
        name: document.getElementById("name").value,
        age: Number(document.getElementById("age").value),
        email: document.getElementById("email").value,
        course: document.getElementById("course").value
    };

    let response;

    if (editId === null) {
        response = await fetch(`${API_URL}/students`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(student)
        });
    } else {
        response = await fetch(`${API_URL}/students/${editId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(student)
        });
    }

    if (response.ok) {
    showToast(
        editId === null ? "Student added successfully!" : "Student updated successfully!"
    );
} else {
    const errorData = await response.json();
    showToast(errorData.detail || "Something went wrong", "error");
}

form.reset();
editId = null;
form.querySelector("button[type='submit']").textContent = "Add Student";

await loadStudents();
});

function editStudent(id, studentData) {
    const student = JSON.parse(decodeURIComponent(studentData));

    editId = id;

    document.getElementById("name").value = student.name;
    document.getElementById("age").value = student.age;
    document.getElementById("email").value = student.email;
    document.getElementById("course").value = student.course;

    form.querySelector("button[type='submit']").textContent = "Update Student";
}

async function deleteStudent(id) {
    const confirmDelete = confirm("Are you sure you want to delete this student?");

    if (!confirmDelete) {
        return;
    }

    const response = await fetch(`${API_URL}/students/${id}`, {
        method: "DELETE"
    });

    if (response.ok) {
    showToast("Student deleted successfully!");
    await loadStudents();
} else {
    showToast("Unable to delete student.", "error");
}
}

loadStudents();
