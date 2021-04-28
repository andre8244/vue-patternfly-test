<template>
  <div id="app">
    <Slider :value="sliderValue" @onChange="onChange" :customSteps="steps" />

    <Button variant="primary" @onClick="click">Primary</Button>

    <DatePicker @onChange="date" />

    <TextInput
      isRequired
      type="text"
      id="simple-form-name-01"
      name="simple-form-name-01"
      aria-describedby="simple-form-name-01-helper"
      :value="text"
      @onChange="change"
    />

    <Modal
          title="Simple modal header"
          :isOpen="open"
          @onClose="handleModalToggle"
          :actions="['aa', 'ff']"
        >
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
          magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
          consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
          est laborum.

          <ModalBoxFooter>
            <Button variant="primary" @onClick="open = false">Primary</Button>
            <Button variant="primary" @onClick="open = false">Primary</Button>
          </ModalBoxFooter>
        </Modal>

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
import { Slider, Button, DatePicker, TextInput, Modal, ModalBoxFooter } from "@patternfly/react-core";

export default {
  name: "App",
  data() {
    return {
      sliderValue: 50,
      steps: [
        { value: 0, label: "0" },
        { value: 12.5, label: "1", isLabelHidden: true },
        { value: 25, label: "2" },
        { value: 37.5, label: "3", isLabelHidden: true },
        { value: 50, label: "4" },
        { value: 62.5, label: "5", isLabelHidden: true },
        { value: 75, label: "6" },
        { value: 87.5, label: "7", isLabelHidden: true },
        { value: 100, label: "8" }
      ],
      text: "ab",
      open: false,
    };
  },
  methods: {
    onChange() {
      console.log("onChange"); ////
    },
    click() {
      console.log("click"); ////
      this.open = true;
    },
    date(a, b) {
      console.log(a, b); ////
    },
    change($event) {
      this.text = $event;
      console.log(this.text);
    },
    handleModalToggle() {
      this.open != this.open;
    }
  },
  components: { Slider, Button, DatePicker, TextInput, Modal, ModalBoxFooter }
};
</script>

<style lang="scss">
@import "./assets/styles/patternfly/patternfly.css";
</style>
