<template>
      <div class="budget-category-table">
        <!-- Table Title -->
        <h2 class="table-title">{{ title }}</h2>

        <!-- Table -->
        <table class="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Starting Value</th>
              <th>+</th>
              <th>-</th>
              <th>Ending Value</th>
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
                  v-model.number="item.startingValue"
                  placeholder="Starting Value"
                  class="form-input formatted-input"
                  @input="notifyModified"
                />
              </td>
              <td>
                <input
                  type="number"
                  v-model.number="item.added"
                  placeholder="+"
                  class="form-input formatted-input"
                  @input="notifyModified"
                />
              </td>
              <td>
                <input
                  type="number"
                  v-model.number="item.subtracted"
                  placeholder="-"
                  class="form-input formatted-input"
                  @input="notifyModified"
                />
              </td>
              <td>
                <span class="ending-value  formatted-input">
                  {{ calculateEndingValue(item.startingValue, item.added, item.subtracted) }}
                </span>
              </td>
              <td>
                <button @click="deleteRow(index)" class="delete-btn">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- Add New Row Button -->
        <button @click="addRow" class="add-row-btn">Add New Row</button>
      </div>
</template>

<script>
export default {
  name: "SinkingFundTable",
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
      const newRow = {
        name: "",
        startingValue: 0,
        added: 0,
        subtracted: 0,
      };
      this.$emit("add-row", newRow); // Emit to the parent to add the row
    },
    deleteRow(index) {
      this.$emit("delete-row", index); // Emit to the parent to delete the row
    },
    calculateEndingValue(startingValue, added, subtracted) {
      const result = startingValue + added - subtracted;
      return Math.round(result * 100) / 100;
    },
    notifyModified() {
      this.$emit("modified"); // Notify parent of data modification
    },
  },
};
</script>
  
  <style scoped>

  </style>
  