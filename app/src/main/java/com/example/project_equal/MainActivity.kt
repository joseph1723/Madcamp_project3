package com.example.project_equal

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.MotionEvent
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val sharedPreferences = getSharedPreferences("login_prefs", Context.MODE_PRIVATE)
        val userId = sharedPreferences.getString("user_id", null)

        if (userId != null) {
            Log.d("MainActivity", "User ID: $userId")
            Toast.makeText(this, "Welcome back, User ID: $userId", Toast.LENGTH_LONG).show()
        } else {
            Log.d("MainActivity", "No login info found, redirecting to LoginActivity")
            Toast.makeText(this, "Please log in", Toast.LENGTH_LONG).show()
            val intent = Intent(this, LoginActivity::class.java)
            startActivity(intent)
            finish()
        }
    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        if (event?.action == MotionEvent.ACTION_DOWN) {
            val intent = Intent(this, HomeActivity::class.java)
            startActivity(intent)
            finish()
            return true
        }
        return super.onTouchEvent(event)
    }
}
