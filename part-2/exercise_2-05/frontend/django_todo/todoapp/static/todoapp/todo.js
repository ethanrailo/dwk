function init() {
  //Event listeners
  const todo_form = document.getElementById("todo_form");
  todo_form.addEventListener("submit", (event) => {
    event.preventDefault();
    submitTodo();
  });

  //Fetch todos in the init-phase
  fetchTodos();
}

//handle sumbitting the new todo
async function submitTodo() {
  const todo_from = document.getElementById("todo_form");
  const formData = new FormData(todo_from);

  try {
    const response = await fetch("/todos/", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("Success:", data);
    fetchTodos();
  } catch (error) {
    console.error("Error:", error);
  }
}

//handle fetching the todos
async function fetchTodos() {
  try {
    const todo_container = document.getElementById("todo-list");
    const response = await fetch("/todos/");

    if (!response.ok) {
      todo_container.innerHTML =
        "<p>Error while fetching todos from backend</p>";
      throw new Error("Problem with the request/response");
    }

    const data = await response.json();

    if (!Object.keys(data).length == 0) {
      const list = document.createElement("ul");

      data.forEach((item) => {
        const listItem = document.createElement("li");
        listItem.textContent = item.fields.todo_text;
        list.appendChild(listItem);
      });

      todo_container.innerHTML = "";
      todo_container.appendChild(list);
    } else {
      todo_container.innerHTML =
        "<p>No todos yet, maybe you should add one?</p>";
    }
  } catch (error) {
    console.error("Fetch error:", error);
  }
}
