<template>
      <div class="budget-category-table">
        <!-- Table Title -->
        <h2 class="table-title">
          <input
            type="text"
            :value="title"
            placeholder="Title"
            class="form-input formatted-input"
            @blur="$emit('update:title', $event.target.value)"
          />
        </h2>

        <!-- Table -->
        <table class="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Starting Value</th>
              <th>+</th>
              <th>-</th>
              <th>Ending Value</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in Categories" :key="index" :class="{'bg-light-red': item.ending_value < 0}">
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
                  v-model.number="item.starting_value"
                  placeholder="Starting Value"
                  class="form-input formatted-input"
                  @input="notifyModified"
                />
              </td>
              <td>
                <input
                  type="number"
                  v-model.number="item.plus"
                  placeholder="+"
                  class="form-input formatted-input"
                  @input="notifyModified"
                />
              </td>
              <td>
                <span class="formatted-value">
              {{ Math.round(item.minus * 100) / 100 }}
            </span>
              </td>
              <td>
                <span class="ending-value  formatted-input">
                  {{ calculateEndingValue(item.starting_value, item.plus, item.minus) }}
                </span>
              </td>
              <td class="no-background">
                <button @click="deleteRow(index)" class="btn btn-danger rounded-circle p-0 delete-btn">X</button>
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
        starting_value: 0,
        plus: 0,
        minus: 0,
        ending_value: 0,
      };
      this.$emit("add-row", newRow); // Emit to the parent to add the row
    },
    deleteRow(index) {
      this.$emit("delete-row", index); // Emit to the parent to delete the row
    },
    calculateEndingValue(startingValue, added, subtracted) {
      return Math.round((startingValue + added - subtracted) * 100) / 100;
    },
    notifyModified() {
      this.$emit("modified"); // Notify parent of data modification
    },
    updateTitle(newTitle) {
      this.$emit("update:title", newTitle); // Emit updated title to parent
      this.notifyModified(); // Notify parent of modification
    },
  },
  watch: {
    Categories: {
      handler(newCategories) {
        // Iterate through categories and recalculate ending_value
        newCategories.forEach((item) => {
          item.ending_value = this.calculateEndingValue(
            item.starting_value,
            item.plus,
            item.minus
          );
        });
      },
      deep: true, // Enable deep watching for nested objects
    },
  },
};

</script>
  
<style scoped>

</style>
  