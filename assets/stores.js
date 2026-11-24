// Liens des stores et bascule « Android » du site — UN SEUL endroit à modifier.
//
// Tant que PLAY_STORE_URL et PLAY_TESTING_URL sont vides, RIEN d'Android ne
// s'affiche : les éléments marqués gardent leur texte actuel (iPhone).
//   - PLAY_TESTING_URL : lien d'inscription au test fermé Google Play
//     (https://play.google.com/apps/testing/com.ecleptic.app). À remplir quand
//     la bêta Android ouvre ET que la colonne beta_testers.phone_platform
//     existe en prod (sinon le formulaire de la bêta serait refusé).
//   - PLAY_STORE_URL : fiche publique Google Play
//     (https://play.google.com/store/apps/details?id=com.ecleptic.app). À
//     remplir le jour de la sortie Android.
//   - APP_STORE_URL : fiche App Store, le jour de la sortie iOS.
// Liste complète de ce qui bascule (pages écrites à la main, générateur,
// balises meta) : Auros/reports/play-store/site-lancement-android.md.
//
// Marquage dans les pages :
//   data-android-text="…"  texte remplacé quand Android est ouvert (bêta ou store) ;
//   data-android-only      élément caché tant qu'Android n'est pas ouvert.
(function () {
  var S = (window.EclepticStores = {
    APP_STORE_URL: "",
    TESTFLIGHT_URL: "https://testflight.apple.com/join/H5CQgDa7",
    PLAY_STORE_URL: "",
    PLAY_TESTING_URL: ""
  });
  S.androidLive = !!(S.PLAY_STORE_URL || S.PLAY_TESTING_URL);
  S.isAndroid = /Android/i.test(navigator.userAgent || "");

  S.apply = function (root) {
    if (!S.androidLive) return;
    var scope = root || document;
    scope.querySelectorAll("[data-android-text]").forEach(function (el) {
      el.textContent = el.getAttribute("data-android-text");
    });
    scope.querySelectorAll("[data-android-only]").forEach(function (el) {
      el.hidden = false;
    });
  };

  // Boutons « App Store » et « Google Play » (ils remplacent l'ancienne page bêta) :
  //   <a class="storebtn" data-store="ios|android" aria-disabled="true">
  //     <small data-live="Télécharger l'application">Bientôt disponible</small><b>App Store</b></a>
  // Sans APP_STORE_URL / PLAY_STORE_URL, le bouton reste inactif (pas de lien). Dès qu'un lien
  // est écrit ci-dessus, le bouton correspondant devient cliquable sur tout le site.
  S.buttons = function (root) {
    (root || document).querySelectorAll("a.storebtn[data-store]").forEach(function (a) {
      var url = a.getAttribute("data-store") === "ios" ? S.APP_STORE_URL : S.PLAY_STORE_URL;
      if (!url) return;
      a.href = url;
      a.rel = "noopener";
      a.removeAttribute("aria-disabled");
      var s = a.querySelector("small[data-live]");
      if (s) s.textContent = s.getAttribute("data-live");
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { S.apply(); S.buttons(); });
  } else {
    S.apply();
    S.buttons();
  }
})();
