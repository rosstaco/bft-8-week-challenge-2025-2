import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
        <p></p>
  );
}

function MealPlansSection() {
  return (
    <section className={styles.features}>
      <div className="container">

        <div className="row">
          <div className="col col--12">
            <div className="text--center padding-horiz--md">
              <Heading as="h2">Weekly Meal Plans</Heading>
              <ul style={{textAlign: 'left', display: 'inline-block'}}>
                <li><Link to="/docs/meal-plans/Week_1_Meal_Plan">Week 1 Meal Plan</Link></li>
                <li><Link to="/docs/meal-plans/Week_2_Meal_Plan">Week 2 Meal Plan</Link></li>
                <li><Link to="/docs/meal-plans/Week_3_Meal_Plan">Week 3 Meal Plan</Link></li>
                <li><Link to="/docs/meal-plans/Week_4_Meal_Plan">Week 4 Meal Plan</Link></li>
                <li><Link to="/docs/meal-plans/Week_5_Meal_Plan">Week 5 Meal Plan</Link></li>
                <li><Link to="/docs/meal-plans/Week_6_Meal_Plan">Week 6 Meal Plan</Link></li>
                <li><Link to="/docs/meal-plans/Week_7_Meal_Plan">Week 7 Meal Plan</Link></li>
                <li><Link to="/docs/meal-plans/Week_8_Meal_Plan">Week 8 Meal Plan</Link></li>
              </ul>
            </div>
          </div>
          
        </div>
        
      </div>
    </section>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Complete 8-week meal planning guide for your fitness transformation">
      <HomepageHeader />
      <main>
        <MealPlansSection />
      </main>
    </Layout>
  );
}
