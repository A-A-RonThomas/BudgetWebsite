<template>
  <div class="layout">
    <!-- Side Navigation -->
    <div class="side-nav">
      <SideNavigation/>
    </div>

    <!-- Main Content Area -->
    <div class="main-content">
      <!-- Top Bar -->
      <div class="top-bar">
        <TopNavigation />
      </div>

      <!-- Route-specific content -->
      <div class="content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import SideNavigation from "./components/SideNavigation.vue";
import TopNavigation from "./components/TopNavigation.vue";

export default {
  name: "App",
  components: {
    SideNavigation,
    TopNavigation,
  },
};
</script>

<style>
/* Layout Styles */
.layout {
  display: flex;
  height: 100vh;
}

.side-nav {
  width: 250px;
  background-color: #f8f9fa;
  border-right: 1px solid #ddd;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.top-bar {
  height: 50px;
  background-color: #fff;
  border-bottom: 1px solid #ddd;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 20px;
}

.content {
  flex-grow: 1;
  padding: 20px;
  background-color: #f1f1f1;
  overflow-y: auto;
}
</style>
