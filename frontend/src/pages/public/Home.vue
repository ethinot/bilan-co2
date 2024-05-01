<template>
  <section class="container mx-auto px-4">
    <h1 class="text-3xl font-bold mb-4">Welcome to Carbon Tracker</h1>
    <p class="text-lg mb-6">
      Carbon Tracker helps you track your carbon emissions and make more
      environmentally friendly choices in your daily life.
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <div class="bg-gray-100 p-6 rounded-lg">
        <h2 class="text-xl font-semibold mb-2">Track Your Emissions</h2>
        <p>
          Log your daily activities and see how much carbon dioxide you're
          emitting. Get personalized tips on reducing your carbon footprint.
        </p>
      </div>
      <div class="bg-gray-100 p-6 rounded-lg">
        <h2 class="text-xl font-semibold mb-2">Dashboard</h2>
        <p>
          Visualize your carbon emissions over time with our interactive
          dashboard. Set goals and monitor your progress towards a greener
          lifestyle.
        </p>
      </div>
    </div>
    <div class="mt-12">
      <h2 class="text-2xl font-bold mb-4">Why Track Carbon Emissions?</h2>
      <p class="text-lg mb-4">
        Tracking your carbon emissions can help you understand your
        environmental impact and make informed decisions to reduce it. Here are
        some reasons why it's important:
      </p>
      <ul class="list-disc list-inside">
        <li>Reduce your carbon footprint</li>
        <li>Contribute to combating climate change</li>
        <li>Save money by reducing energy consumption</li>
        <li>Lead a more sustainable lifestyle</li>
      </ul>
    </div>
    <div class="mt-12">
      <h2 class="text-2xl font-bold mb-4">Get Started Today!</h2>
      <p class="text-lg mb-4">
        Ready to start tracking your carbon emissions and making a positive
        impact on the environment? Sign up now and join our community of
        eco-conscious individuals!
      </p>
      <router-link
        to="/register"
        class="inline-block px-6 py-3 bg-green-500 text-white rounded-md font-semibold"
        >Sign Up</router-link
      >
    </div>
  </section>
</template>
