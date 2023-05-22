<template>

  <div class="container">
    <h2>Введите ваше имя и почту</h2>
    <form>
      <input type="text" id="name" placeholder="Ваше имя" required>
      <input type="text" id="phone" placeholder="Ваш телефон" required>
      <input type="button" value="Отправить" @click="sendData">
    </form>
    </div>

</template>
<script>

export default {
methods:{
      sendData() {
        let name = document.getElementById("name").value;
        let phone = document.getElementById("phone").value;

        let data = {
          name: name,
          phone: phone
        };

        let xhr = new XMLHttpRequest();
        xhr.open("POST", "http://127.0.0.1:8000/api/create_appeal", true);
        xhr.setRequestHeader("Content-Type", "application/json");


        xhr.send(JSON.stringify(data));
    }
}
}

  </script>

  <style scoped>

.container {
      width: 300px;
      margin: 0 auto;
      padding: 20px;
    }

.container input[type="text"],
.container input[type="submit"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
    }

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>