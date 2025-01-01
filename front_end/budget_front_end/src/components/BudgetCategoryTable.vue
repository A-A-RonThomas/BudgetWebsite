<template>
  <div class="budget-category-table">
    <h2 class="table-title">{{ title }}</h2>
    <table class="table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Expected</th>
          <th>Actual</th>
          <th>Budget Category</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in Categories" :key="index">
          <td>
  <input
    type="text"
    v-model="item.name"
    placeholder="Name"
    class="form-input formatted-input"
    @input="notifyModified"
  />
</td>
<td>
  <input
    type="number"
    v-model.number="item.expected"
    placeholder="Expected"
    class="form-input formatted-input"
    @input="notifyModified"
  />
</td>
<td>
  <input
    type="number"
    v-model.number="item.actual"
    placeholder="Actual"
    class="form-input formatted-input"
    @input="notifyModified"
  />
</td>
<td>
  <input
    type="text"
    v-model="item.category"
    placeholder="Category"
    class="form-input formatted-input"
    @input="notifyModified"
  />
</td>
          <td>
            <button @click="deleteRow(index)" class="delete-btn">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    <button @click="addRow" class="add-row-btn">Add New Row</button>
  </div>
</template>

<script>
export default {
  name: "BudgetCategoryTable",
  props: {
    title: {
      type: String,
      required: true,
    },
    Categories: {
      type: Array,
      required: true,
    },
  },
  methods: {
    addRow() {
      const newCategory = {
        name: "",
        expected: 0,
        actual: 0,
        category: "",
      };
      this.$emit("add-row", newCategory); // Notify parent to add a row
      this.notifyModified(); // Notify parent of modification
    },
    deleteRow(index) {
      this.$emit("delete-row", index); // Notify parent to delete a row
      this.notifyModified(); // Notify parent of modification
    },
    notifyModified() {
      this.$emit("modified"); // Notify parent of data modification
    },
  },
};
</script>


<style scoped>


</style>
