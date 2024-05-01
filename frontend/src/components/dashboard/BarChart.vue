<template>
  <Bar id="my-chart-id" :options="chartOptions" :data="chartData" />
</template>

<script>
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: { Bar },
  props: ["data"],
  data() {
    return {
      chartOptions: {
        responsive: true,
        colors: {
          enabled: true,
        },
      },
    };
  },
  computed: {
    chartData() {
      return {
        labels: ["Trips", "Energy", "Food"],
        datasets: [
          {
            label: "Emission by Category",
            data: this.data,
            backgroundColor: [
              "rgba(255, 99, 132)",
              "rgba(255, 159, 64)",
              "rgba(255, 205, 86)",
            ],
          },
        ],
      };
    },
  },
};
</script>
