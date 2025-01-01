// saveOnExitMixin.js
export default {
    created() {
      window.addEventListener("beforeunload", this.handleBeforeUnload);
    },
  
    beforeDestroy() {
      window.removeEventListener("beforeunload", this.handleBeforeUnload);
    },
  
    beforeRouteLeave(to, from, next) {
      if (this.hasUnsavedChanges()) {
        this.saveBudgets()
          .then(() => next())
          .catch((error) => {
            console.error("Error saving on route change:", error);
            next(); // Allow navigation even if saving fails
          });
      } else {
        next();
      }
    },
  
    methods: {
      handleBeforeUnload(event) {
        if (this.hasUnsavedChanges()) {
          this.saveBudgets();
          event.preventDefault();
          event.returnValue = "";
        }
      },
  
      // Placeholder methods - must be implemented in components using the mixin
      hasUnsavedChanges() {
        console.warn("hasUnsavedChanges not implemented in component");
        return false;
      },
  
      async saveBudgets() {
        console.warn("saveBudgets not implemented in component");
        return Promise.resolve();
      },
    },
  };
  