using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;
using System.Collections;

public class PlayerController : MonoBehaviour
{
    Rigidbody2D rb;
    public float jumpPower;
    public GameObject startText;

    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        rb.gravityScale = 0;

        Slider slider = GameObject.Find("fuel")?.GetComponent<Slider>();
        if (slider != null)
            GameManager.Instance.SetFuelSlider(slider);
        else
            Debug.LogError("Fuel slider not found");

        GameManager.Instance.ResetFuel();
    }

    void Update()
    {
        if (!GameManager.gameStarted && Input.GetMouseButtonDown(0))
        {
            StartGame();
        }
        else if (GameManager.gameStarted && Input.GetMouseButtonDown(0))
        {
            Jump();
        }
    }

    void StartGame()
    {
        GameManager.gameStarted = true;
        rb.gravityScale = 1;
        rb.velocity = Vector2.up * jumpPower;
        startText.SetActive(false);

        if (GameManager.Instance.UseFuel())
            GetComponent<AudioSource>().Play();
    }

    void Jump()
    {
        if (GameManager.Instance.UseFuel())
        {
            rb.velocity = Vector2.up * jumpPower;
            GetComponent<AudioSource>().Play();
        }
        else
        {
            EndGame();
        }
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        EndGame();
    }

    private void EndGame()
    {
        ScoreManager.Instance.SaveScore();

       // StartCoroutine(FindObjectOfType<ScoreAPI>().SendScore(ScoreManager.Instance.Score));

        SceneManager.LoadScene("GameOverScene");
    }
}
