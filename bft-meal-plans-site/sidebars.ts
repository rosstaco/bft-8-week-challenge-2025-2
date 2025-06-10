import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // Create a manual sidebar for better organization
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Weekly Meal Plans',
      items: [
        'meal-plans/Week_1_Meal_Plan',
        'meal-plans/Week_2_Meal_Plan',
        'meal-plans/Week_3_Meal_Plan',
        'meal-plans/Week_4_Meal_Plan',
        'meal-plans/Week_5_Meal_Plan',
        'meal-plans/Week_6_Meal_Plan',
        'meal-plans/Week_7_Meal_Plan',
        'meal-plans/Week_8_Meal_Plan',
      ],
    },
  ],
};

export default sidebars;
