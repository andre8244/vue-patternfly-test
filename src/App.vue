<template>
  <div id="app">
    <div class="pf-c-page" id="primary-detail-panel-body-padding">
      <a
        class="pf-c-skip-to-content pf-c-button pf-m-primary"
        href="#main-content-primary-detail-panel-body-padding"
        >Skip to content</a
      >
      <header class="pf-c-page__header">
        <div class="pf-c-page__header-brand">
          <div class="pf-c-page__header-brand-toggle">
            <button
              class="pf-c-button pf-m-plain"
              type="button"
              id="primary-detail-panel-body-padding-nav-toggle"
              aria-label="Global navigation"
              aria-expanded="true"
              aria-controls="primary-detail-panel-body-padding-primary-nav"
            >
              <i class="fas fa-bars" aria-hidden="true"></i>
            </button>
          </div>
          <!-- <a href="#" class="pf-c-page__header-brand-link"> -->
          <!-- <img
              class="pf-c-brand"
              src="/assets/images/PF-Masthead-Logo.svg"
              alt="PatternFly logo"
            /> -->
          <div class="pf-c-content">
            <h1>NethSecurity</h1>
          </div>
          <!-- </a> -->
        </div>
        <div class="pf-c-page__header-tools">
          <div class="pf-c-page__header-tools-group">
            <div
              class="pf-c-page__header-tools-item pf-m-hidden pf-m-visible-on-lg"
            >
              <button
                class="pf-c-button pf-m-plain"
                type="button"
                aria-label="Settings"
              >
                <i class="fas fa-cog" aria-hidden="true"></i>
              </button>
            </div>
            <div
              class="pf-c-page__header-tools-item pf-m-hidden pf-m-visible-on-lg"
            >
              <button
                class="pf-c-button pf-m-plain"
                type="button"
                aria-label="Help"
              >
                <i class="pf-icon pf-icon-help" aria-hidden="true"></i>
              </button>
            </div>
          </div>
          <div class="pf-c-page__header-tools-group">
            <div class="pf-c-page__header-tools-item pf-m-hidden-on-lg">
              <div class="pf-c-dropdown pf-m-expanded">
                <button
                  class="pf-c-dropdown__toggle pf-m-plain"
                  id="primary-detail-panel-body-padding-dropdown-kebab-1-button"
                  aria-expanded="false"
                  type="button"
                  aria-label="Actions"
                >
                  <i class="fas fa-ellipsis-v" aria-hidden="true"></i>
                </button>
                <ul
                  class="pf-c-dropdown__menu pf-m-align-right"
                  aria-labelledby="primary-detail-panel-body-padding-dropdown-kebab-1-button"
                  hidden
                >
                  <li>
                    <a class="pf-c-dropdown__menu-item" href="#">Link</a>
                  </li>
                  <li>
                    <button class="pf-c-dropdown__menu-item" type="button">
                      Action
                    </button>
                  </li>
                  <li>
                    <a
                      class="pf-c-dropdown__menu-item pf-m-disabled"
                      href="#"
                      aria-disabled="true"
                      tabindex="-1"
                      >Disabled link</a
                    >
                  </li>
                  <li>
                    <button
                      class="pf-c-dropdown__menu-item"
                      type="button"
                      disabled
                    >
                      Disabled action
                    </button>
                  </li>
                  <li class="pf-c-divider" role="separator"></li>
                  <li>
                    <a class="pf-c-dropdown__menu-item" href="#"
                      >Separated link</a
                    >
                  </li>
                </ul>
              </div>
            </div>
            <div
              class="pf-c-page__header-tools-item pf-m-hidden pf-m-visible-on-md"
            >
              <div class="pf-c-dropdown">
                <button
                  class="pf-c-dropdown__toggle"
                  id="primary-detail-panel-body-padding-dropdown-kebab-2-button"
                  aria-expanded="false"
                  type="button"
                >
                  <span class="pf-c-dropdown__toggle-text">John Smith</span>
                  <span class="pf-c-dropdown__toggle-icon">
                    <i class="fas fa-caret-down" aria-hidden="true"></i>
                  </span>
                </button>
                <ul
                  class="pf-c-dropdown__menu"
                  aria-labelledby="primary-detail-panel-body-padding-dropdown-kebab-2-button"
                  hidden
                >
                  <li>
                    <a class="pf-c-dropdown__menu-item" href="#">Link</a>
                  </li>
                  <li>
                    <button class="pf-c-dropdown__menu-item" type="button">
                      Action
                    </button>
                  </li>
                  <li>
                    <a
                      class="pf-c-dropdown__menu-item pf-m-disabled"
                      href="#"
                      aria-disabled="true"
                      tabindex="-1"
                      >Disabled link</a
                    >
                  </li>
                  <li>
                    <button
                      class="pf-c-dropdown__menu-item"
                      type="button"
                      disabled
                    >
                      Disabled action
                    </button>
                  </li>
                  <li class="pf-c-divider" role="separator"></li>
                  <li>
                    <a class="pf-c-dropdown__menu-item" href="#"
                      >Separated link</a
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <!-- <img
            class="pf-c-avatar"
            src="/assets/images/img_avatar.svg"
            alt="Avatar image"
          /> -->
          <!-- <font-awesome-icon icon="user" /> -->
        </div>
      </header>
      <div class="pf-c-page__sidebar">
        <div class="pf-c-page__sidebar-body">
          <nav
            class="pf-c-nav"
            id="primary-detail-panel-body-padding-primary-nav"
            aria-label="Global"
          >
            <ul class="pf-c-nav__list">
              <li class="pf-c-nav__item">
                <a
                  href="#"
                  class="pf-c-nav__link pf-m-current"
                  aria-current="page"
                  >Firewall</a
                >
              </li>
              <li class="pf-c-nav__item">
                <a href="#" class="pf-c-nav__link">Policy</a>
              </li>
              <li class="pf-c-nav__item">
                <a href="#" class="pf-c-nav__link">Authentication</a>
              </li>
              <li class="pf-c-nav__item">
                <a href="#" class="pf-c-nav__link">Network services</a>
              </li>
              <li class="pf-c-nav__item">
                <a href="#" class="pf-c-nav__link">Server</a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
      <main class="pf-c-page__main" tabindex="-1">
        <section class="pf-c-page__main-breadcrumb pf-m-limit-width">
          <div class="pf-c-page__main-body">
            <nav class="pf-c-breadcrumb" aria-label="breadcrumb">
              <ol class="pf-c-breadcrumb__list">
                <li class="pf-c-breadcrumb__item">
                  <a href="#" class="pf-c-breadcrumb__link">Section home</a>
                </li>
                <li class="pf-c-breadcrumb__item">
                  <span class="pf-c-breadcrumb__item-divider">
                    <i class="fas fa-angle-right" aria-hidden="true"></i>
                  </span>
                  <a href="#" class="pf-c-breadcrumb__link">Section title</a>
                </li>
                <li class="pf-c-breadcrumb__item">
                  <span class="pf-c-breadcrumb__item-divider">
                    <i class="fas fa-angle-right" aria-hidden="true"></i>
                  </span>
                  <a href="#" class="pf-c-breadcrumb__link">Section title</a>
                </li>
                <li class="pf-c-breadcrumb__item">
                  <span class="pf-c-breadcrumb__item-divider">
                    <i class="fas fa-angle-right" aria-hidden="true"></i>
                  </span>
                  <a
                    href="#"
                    class="pf-c-breadcrumb__link pf-m-current"
                    aria-current="page"
                    >Section landing</a
                  >
                </li>
              </ol>
            </nav>
          </div>
        </section>
        <section class="pf-c-page__main-section pf-m-light">
          <div class="pf-c-content">
            <h1>Firewall rules</h1>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
              eiusmod tempor incididunt ut labore et dolore magna aliqua.
            </p>
          </div>
        </section>
        <div class="pf-c-divider" role="separator"></div>
        <section class="pf-c-page__main-section pf-m-no-padding">
          <!-- Drawer -->
          <div class="pf-c-drawer pf-m-expanded pf-m-inline-on-2xl">
            <div class="pf-c-drawer__main">
              <!-- Content -->
              <div class="pf-c-drawer__content pf-m-no-background">
                <div class="pf-c-drawer__body pf-m-padding">
                  <button
                    class="pf-c-button pf-m-primary mg-b-1"
                    type="button"
                    @click="openModal"
                  >
                    Create rule
                  </button>
                  <!-- empty state -->
                  <div v-if="!fwaConfig.rules.length" class="pf-c-empty-state">
                    <div class="pf-c-empty-state__content">
                      <i
                        class="fas fa-shield-alt pf-c-empty-state__icon"
                        aria-hidden="true"
                      ></i>
                      <h1 class="pf-c-title pf-m-lg">No rule</h1>
                      <div class="pf-c-empty-state__body">
                        No firewall rule configured
                      </div>
                      <button
                        class="pf-c-button pf-m-primary"
                        type="button"
                        @click="openModal"
                      >
                        Create rule
                      </button>
                    </div>
                  </div>
                  <!-- rule list -->
                  <div v-else>
                    <ul
                      class="pf-c-data-list"
                      role="list"
                      aria-label="Checkbox and action data list example"
                      id="data-list-checkboxes-actions-addl-cells"
                    >
                      <li
                        v-for="(rule, index) in fwaConfig.rules"
                        :key="index"
                        class="pf-c-data-list__item"
                        aria-labelledby="data-list-checkboxes-actions-addl-cells-item-1"
                      >
                        <div class="pf-c-data-list__item-row">
                          <div class="pf-c-data-list__item-control">
                            <button
                              class="pf-c-data-list__item-draggable-button"
                              type="button"
                              aria-label="Reorder"
                              aria-pressed="false"
                              id="data-list-draggable-draggable-button-2"
                              aria-describedby="draggable-help"
                              aria-labelledby="data-list-draggable-draggable-button-2 data-list-draggable-item-2"
                            >
                              <span class="pf-c-data-list__item-draggable-icon">
                                <i class="fas fa-grip-vertical"></i>
                              </span>
                            </button>
                          </div>
                          <div class="pf-c-data-list__item-content">
                            <div class="pf-c-data-list__cell">
                              <span><i class="fas fa-ban mg-r-05"></i></span>
                              <span>Block</span>
                            </div>
                            <div class="pf-c-data-list__cell">
                              <span>
                                <font-awesome-icon
                                  :icon="['fab', getAppIcon(rule.application)]"
                                  class="mg-r-05"
                                />
                              </span>
                              <span>{{ getAppName(rule.application) }}</span>
                            </div>
                          </div>
                          <div class="pf-c-data-list__item-action">
                            <div class="pf-c-data-list__action">
                              <button
                                class="pf-c-button pf-m-danger"
                                type="button"
                              >
                                Delete
                              </button>
                            </div>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <!-- Panel -->
              <div class="pf-c-drawer__panel">
                <!-- Panel header -->
                <div class="pf-c-drawer__body">
                  <div class="pf-l-flex pf-m-column">
                    <div class="pf-l-flex__item">
                      <div class="pf-c-drawer__head">
                        <div class="pf-c-drawer__actions">
                          <div class="pf-c-drawer__close">
                            <button
                              class="pf-c-button pf-m-plain"
                              type="button"
                              aria-label="Close drawer panel"
                            >
                              <i class="fas fa-times" aria-hidden="true"></i>
                            </button>
                          </div>
                        </div>
                        <h2
                          class="pf-c-title pf-m-lg"
                          id="primary-detail-panel-body-padding-drawer-label"
                        >
                          Netify-fwa config
                        </h2>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- Tab content -->
                <div class="pf-c-drawer__body">
                  <div class="pf-l-flex pf-m-column pf-m-space-items-lg">
                    <pre class="mg-y-1">{{
                      JSON.stringify(fwaConfig, null, 2)
                    }}</pre>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>

    <!-- new rule modal -->
    <div
      class="pf-c-modal-box pf-m-sm modal"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-sm-title"
      aria-describedby="modal-sm-description"
      v-if="showModal"
    >
      <button
        class="pf-c-button pf-m-plain"
        type="button"
        aria-label="Close dialog"
        @click="closeDialog"
      >
        <i class="fas fa-times" aria-hidden="true"></i>
      </button>
      <header class="pf-c-modal-box__header">
        <h1 class="pf-c-modal-box__title" id="modal-sm-title">Create rule</h1>
      </header>
      <div class="pf-c-modal-box__body" id="modal-sm-description">
        <div class="display-flex">
          <div class="pf-c-tile width-half" tabindex="0">
            <div class="pf-c-tile__header pf-m-stacked">
              <div class="pf-c-tile__icon">
                <i class="fas fa-bell" aria-hidden="true"></i>
              </div>
              <div class="pf-c-tile__title">
                Block an application or a protocol
              </div>
            </div>
            <div class="pf-c-tile__body">
              Detect and block traffic for Facebook, YouTube or other apps
            </div>
          </div>
          <div class="pf-c-tile width-half" tabindex="0">
            <div class="pf-c-tile__header pf-m-stacked">
              <div class="pf-c-tile__icon">
                <i class="fas fa-bell" aria-hidden="true"></i>
              </div>
              <div class="pf-c-tile__title">Create a rule manually</div>
            </div>
            <div class="pf-c-tile__body">
              Specify source, destination, action and other options
            </div>
          </div>
        </div>
      </div>
      <footer class="pf-c-modal-box__footer">Modal footer</footer>
    </div>
  </div>
</template>

<script>
import to from "await-to-js";
import _capitalize from "lodash/capitalize";

export default {
  name: "App",
  data() {
    return {
      fwaConfig: {
        rules: [],
        whitelist: [],
      },
      appIconMap: {
        "netify.facebook": "facebook-square",
        "netify.youtube": "youtube",
        "netify.twitter": "twitter",
      },
      showModal: false,
    };
  },
  created() {
    this.getFwaConfig();
  },
  methods: {
    async getFwaConfig() {
      let errAxios, response;

      [errAxios, response] = await to(
        this.axios.get(`http://192.168.1.1:5000/fwa`)
      );
      if (errAxios) {
        console.error(errAxios);
      }

      this.fwaConfig = response.data;
    },
    async testApi(path) {
      let errAxios, response;

      [errAxios, response] = await to(
        this.axios.get(`http://192.168.1.1:5000/${path}`)
      );
      if (errAxios) {
        console.error(errAxios);
      }
      console.log("response", response); ////

      this.output = response.data;
    },
    getAppName(netifyAppName) {
      return _capitalize(netifyAppName.replaceAll("netify.", ""));
    },
    getAppIcon(netifyAppName) {
      return this.appIconMap[netifyAppName];
    },
    openModal() {
      this.showModal = true;
    },
    closeDialog() {
      this.showModal = false;
    },
  },
};
</script>

<style lang="scss">
@import "./assets/styles/patternfly/patternfly.css";

#app {
  height: 100%;
}

.mg-r-05 {
  margin-right: 0.5rem;
}

.mg-b-1 {
  margin-bottom: 1rem;
}

.mg-y-1 {
  margin-top: 1rem;
  margin-bottom: 1rem;
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -webkit-box-shadow: 0px 0px 50px 20px #000000 !important;
  box-shadow: 0px 0px 80px 30px #666666 !important;
}

.width-half {
  // width: 50%; ////
}

.display-flex {
  display: flex;
}
</style>
