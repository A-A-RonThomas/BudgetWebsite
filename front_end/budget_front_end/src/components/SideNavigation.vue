<template>
  <nav class="nav">
    <ul>
      <li><router-link to="/">Budget</router-link></li>
      <li><router-link to="/purchases">Purchases</router-link></li>
      <li><router-link to="/incomes">Incomes</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "SideNavigation",
};
</script>

<style scoped>
.nav {
  display: flex;
  flex-direction: column;
  padding: 10px;
}

.nav ul {
  list-style: none;
  padding: 0;
}

.nav ul li {
  margin-bottom: 10px;
}

.nav ul li a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  transition: color 0.3s;
}

.nav ul li a:hover {
  color: #007bff;
}
</style>
