<template>
  <div id="app">
    <button class="pf-c-button pf-m-primary" type="button">Primary</button>
    <button class="pf-c-button pf-m-secondary" type="button">Secondary</button>
    <button class="pf-c-button pf-m-tertiary" type="button">Tertiary</button>
    <button class="pf-c-button pf-m-danger" type="button">Danger</button>
    <button class="pf-c-button pf-m-warning" type="button">Warning</button>
    <br />
    <br />
    <button class="pf-c-button pf-m-link" type="button">
      <span class="pf-c-button__icon pf-m-start">
        <i class="fas fa-plus-circle" aria-hidden="true"></i> </span
      >Link
    </button>
    <button class="pf-c-button pf-m-link" type="button">
      Link
      <span class="pf-c-button__icon pf-m-end">
        <i class="fas fa-plus-circle" aria-hidden="true"></i>
      </span>
    </button>
    <button class="pf-c-button pf-m-inline pf-m-link" type="button">
      Inline link
    </button>
    <br />
    <br />
    <button class="pf-c-button pf-m-plain" type="button" aria-label="Remove">
      <i class="fas fa-times" aria-hidden="true"></i>
    </button>
    <br />
    <br />
    <button class="pf-c-button pf-m-control" type="button">Control</button>
    <button
      class="pf-c-button pf-m-control"
      type="button"
      aria-label="Copy input"
    >
      <i class="fas fa-copy" aria-hidden="true"></i>
    </button>
    <br />
    <br />
    <br />
    <button class="pf-c-button pf-m-primary pf-m-small" type="button">
      Primary
    </button>
    <button class="pf-c-button pf-m-secondary pf-m-small" type="button">
      Secondary
    </button>
    <button class="pf-c-button pf-m-tertiary pf-m-small" type="button">
      Tertiary
    </button>
    <button class="pf-c-button pf-m-danger pf-m-small" type="button">
      Danger
    </button>
    <button class="pf-c-button pf-m-warning pf-m-small" type="button">
      Warning
    </button>
    <button class="pf-c-button pf-m-link pf-m-small" type="button">
      Link
      <span class="pf-c-button__icon pf-m-end">
        <i class="fas fa-plus-circle" aria-hidden="true"></i>
      </span>
    </button>
    <button class="pf-c-button pf-m-inline pf-m-link pf-m-small" type="button">
      Inline link
    </button>
    <button class="pf-c-button pf-m-control pf-m-small" type="button">
      Control
    </button>
  </div>
</template>

<script>

export default {
  name: "App",
};
</script>

<style lang="scss">
@import './assets/styles/patternfly/patternfly.css';
</style>
