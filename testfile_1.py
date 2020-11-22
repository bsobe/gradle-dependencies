testOutput = """
------------------------------------------------------------
Project :trendyol_v2
------------------------------------------------------------

prodRuntimeClasspath - Runtime classpath of compilation 'prod' (target  (androidJvm)).
+--- androidx.databinding:databinding-common:4.0.1
+--- androidx.databinding:databinding-runtime:4.0.1
+--- androidx.databinding:databinding-adapters:4.0.1
+--- org.jetbrains.kotlin:kotlin-android-extensions-runtime:1.4.0
+--- project :osiris
+--- project :scalinglib
+--- project :libraries:remote
+--- project :libraries:local
+--- project :features:common (*)
+--- project :features:cart-operations
+--- project :features:configuration
+--- project :features:location-search
+--- project :features:user-operations
+--- project :libraries:extensions (*)
+--- project :features:model (*)
+--- project :features:legacy (*)
+--- project :features:advertisingid (*)
+--- project :libraries:deeplink-dispatcher
+--- project :features:ab-test
+--- project :libraries:widgets
+--- project :features:seller-store
+--- project :libraries:vertical-product-card-view (*)
+--- project :features:in-app-popup
+--- project :features:address:operations
+--- project :features:checkout
+--- project :features:analytics
+--- project :features:seller-review
+--- project :features:order-detail (*)
+--- project :features:base (*)
+--- project :libraries:trace (*)
+--- project :features:authentication
+--- project :features:segmented-user (*)
+--- project :features:contracts (*)
+--- project :features:address:ui
+--- project :libraries:image-loader
+--- project :libraries:image-viewer
+--- project :libraries:boutique-count-down-view (*)
+--- project :shared-data (*)
+--- project :libraries:card-operations
+--- project :features:selectiondialog
+--- project :libraries:showcase-data
+--- project :dolap-lite:ui-components (*)
+--- project :dolap-lite:common (*)
+--- project :dolap-lite:product-detail
+--- project :dolap-lite:checkout
+--- project :dolap-lite:address:address-ui
+--- project :dolap-lite:address:address-data (*)
+--- project :dolap-lite:address:address-communication (*)
+--- project :dolap-lite:dolaplite-homepage (*)
+--- project :dolap-lite:deep-link (*)
+--- project :dolap-lite:orders
+--- project :dolap-lite:search:search-suggestion (*)
+--- project :dolap-lite:search:search-ui
+--- project :dolap-lite:search:search-data (*)
+--- project :dolap-lite:analytics (*)
+--- project :dolap-lite:authentication:authentication-domain (*)
+--- project :dolap-lite:authentication:authentication-remote (*)
+--- project :dolap-lite:data:local-data (*)
+--- project :dolap-lite:data:remote-data (*)
+--- project :dolap-lite:data:content (*)
+--- project :dolap-lite:authentication:authentication-local (*)
+--- project :dolap-lite:filters (*)
+--- project :dolap-lite:paging (*)
+--- project :dolap-lite:favorite-operations (*)
+--- project :dolap-lite:favorite-listing (*)
+--- project :dolap-lite:product-card (*)
+--- project :dolap-lite:product (*)
+--- project :dolap-lite:dolap-lite
+--- project :instant-delivery:local
+--- project :features:scheduled-delivery (*)
+--- project :meal:local
+--- org.jetbrains.kotlin:kotlin-stdlib:1.3.61 -> 1.4.0 (*)
+--- com.google.dagger:dagger:2.26 -> 2.27 (*)
+--- com.google.dagger:dagger-android:2.26 (*)
+--- com.google.dagger:dagger-android-support:2.26 (*)
+--- com.trendyol.android-core:base:1.0.4 (*)
+--- com.trendyol.android-core:android-extensions:1.0.7 (*)
+--- com.trendyol.android-core:lifecycle-extensions:1.0.1 (*)
+--- com.trendyol.android-core:generic-extensions:1.0.5 (*)
+--- androidx.localbroadcastmanager:localbroadcastmanager:1.0.0 (*)
+--- javax.inject:javax.inject:1
+--- androidx.appcompat:appcompat:1.1.0 (*)
+--- androidx.core:core:1.1.0 -> 1.2.0 (*)
+--- androidx.fragment:fragment:1.1.0 -> 1.2.1 (*)
+--- androidx.browser:browser:1.0.0 (*)
+--- androidx.appcompat:appcompat-resources:1.1.0 (*)
+--- androidx.recyclerview:recyclerview:1.0.0 -> 1.1.0 (*)
+--- com.google.android.material:material:1.1.0 (*)
+--- androidx.cardview:cardview:1.0.0 (*)
+--- androidx.constraintlayout:constraintlayout:1.1.3 (*)
+--- androidx.transition:transition:1.2.0 (*)
+--- com.google.firebase:firebase-common:19.3.0 (*)
+--- com.google.firebase:firebase-messaging:20.2.3 (*)
+--- com.google.firebase:firebase-appindexing:19.1.0
+--- com.google.firebase:firebase-auth:19.3.2 (*)
+--- com.google.firebase:firebase-config:19.2.0 (*)
+--- com.google.firebase:firebase-iid:20.2.3 (*)
+--- com.google.android.gms:play-services-auth:17.0.0 (*)
+--- com.google.android.gms:play-services-auth-api-phone:17.4.0 (*)
+--- com.google.android.gms:play-services-gcm:17.0.0
+--- com.google.android.play:core:1.6.3
+--- com.google.android.gms:play-services-maps:17.0.0 (*)
+--- com.google.android.gms:play-services-basement:17.2.1 (*)
+--- com.google.android.gms:play-services-measurement-api:17.4.4 (*)
+--- com.google.android.gms:play-services-ads-identifier:17.0.0 (*)
+--- com.google.android.gms:play-services-iid:17.0.0 (*)
+--- com.google.android.gms:play-services-tasks:17.0.2 (*)
+--- com.google.android.gms:play-services-base:17.1.0 (*)
+--- com.google.firebase:firebase-crashlytics:17.1.0 (*)
+--- com.facebook.stetho:stetho:1.5.1 (*)
+--- com.newrelic.agent.android:android-agent:5.27.1
+--- com.github.arturogutierrez:badges:1.0.5
+--- com.trendyol.android-core:reporter:1.1.0 (*)
+--- com.salesforce.marketingcloud:marketingcloudsdk:7.1.0 (*)
+--- com.facebook.android:facebook-core:7.1.0 (*)
+--- com.facebook.android:facebook-common:7.1.0 (*)
+--- com.facebook.android:facebook-applinks:7.1.0 (*)
+--- com.adjust.sdk:adjust-android:4.21.0
+--- com.adjust.sdk:adjust-android-criteo:4.21.0
+--- com.squareup.okhttp3:okhttp:3.12.2 -> 3.12.10 (*)
+--- com.squareup.okhttp3:logging-interceptor:3.12.2 (*)
+--- com.google.code.gson:gson:2.8.5 -> 2.8.6
+--- com.squareup.retrofit2:retrofit:2.5.0 (*)
+--- com.squareup.retrofit2:converter-gson:2.5.0 (*)
+--- com.squareup.retrofit2:adapter-rxjava2:2.5.0 (*)
+--- com.trendyol.android-core:resource:1.0.3 (*)
+--- com.trendyol.android-core:status:1.0.0 (*)
+--- com.trendyol.android-core:annotation:1.1.0 (*)
+--- io.reactivex.rxjava2:rxandroid:2.1.0 -> 2.1.1 (*)
+--- io.reactivex.rxjava2:rxjava:2.2.3 -> 2.2.17 (*)
+--- com.jakewharton.rxbinding2:rxbinding:2.2.0 (*)
+--- com.commit451:PhotoView:1.2.4 (*)
+--- com.github.Trendyol:StateLayout:1.4.4 (*)
+--- com.roughike:bottom-bar:2.3.1 (*)
+--- com.beloo.widget:ChipsLayoutManager:0.3.7
+--- com.github.MertNYuksel:CircleIndicator:2a2e973374 (*)
+--- com.google.android:flexbox:1.1.0
+--- de.hdodenhof:circleimageview:2.2.0
+--- androidx.core:core-ktx:1.0.1 -> 1.1.0 (*)
+--- com.facebook.shimmer:shimmer:0.5.0 (*)
+--- com.github.erkutaras:impression:0.0.3 (*)
+--- com.github.Trendyol:showcase:0.8 (*)
+--- com.github.Trendyol:medusa:0.9.1-rc (*)
+--- com.github.Trendyol.android-ui-components:dialogs:dialogs-1.0.19 (*)
+--- com.github.Trendyol.android-ui-components:suggestion-input-view:suggestion-input-view-1.1.0
+--- com.github.Trendyol.android-ui-components:card-input-view:card-input-view-1.0.5
+--- com.github.Trendyol.android-ui-components:quantity-picker-view:quantity-picker-view-1.2.1
+--- com.github.Trendyol.android-ui-components:phonenumber:phonenumber-1.0.2 (*)
+--- com.github.Trendyol.android-ui-components:toolbar:toolbar-1.2.3 (*)
+--- com.github.Trendyol.android-ui-components:timeline-view:timeline-view-1.0.0
+--- com.github.Trendyol.android-ui-components:fit-option-message-view:52e0cb60c8
+--- com.google.android.libraries.places:places:2.2.0
+--- com.github.Trendyol.android-ui-components:image-slider:image-slider-1.0.6 (*)
+--- com.github.Trendyol.android-ui-components:touch-delegator:touch-delegator-1.0.0 (*)
+--- androidx.swiperefreshlayout:swiperefreshlayout:1.1.0 (*)
+--- com.jakewharton.rxbinding3:rxbinding-recyclerview:3.1.0 (*)
+--- androidx.viewpager:viewpager:1.0.0 (*)
+--- androidx.viewpager2:viewpager2:1.0.0 (*)
+--- androidx.drawerlayout:drawerlayout:1.0.0 (*)
+--- androidx.coordinatorlayout:coordinatorlayout:1.1.0 (*)
+--- com.github.Trendyol:android-ui-components:rating-bar-1.0.2 (*)
+--- androidx.room:room-rxjava2:2.2.3 (*)
+--- androidx.room:room-runtime:2.2.3 -> 2.2.5 (*)
+--- androidx.room:room-common:2.2.3 -> 2.2.5 (*)
+--- androidx.sqlite:sqlite:2.1.0 (*)
+--- androidx.lifecycle:lifecycle-extensions:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-runtime:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-common:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-livedata-core:2.0.0 -> 2.2.0 (*)
+--- androidx.lifecycle:lifecycle-viewmodel:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-process:2.2.0 (*)
+--- androidx.lifecycle:lifecycle-livedata:2.2.0 (*)
+--- androidx.arch.core:core-common:2.1.0 (*)
+--- com.github.chuckerteam.chucker:library:3.2.0 (*)
+--- project :performance-noop
\--- com.squareup.leakcanary:leakcanary-android:2.0-alpha-2
     +--- com.squareup.leakcanary:leakcanary-android-core:2.0-alpha-2
     \--- org.jetbrains.kotlin:kotlin-stdlib:1.3.21 -> 1.4.0 (*)

(*) - dependencies omitted (listed previously)

A web-based, searchable dependency report is available by adding the --scan option.
"""
